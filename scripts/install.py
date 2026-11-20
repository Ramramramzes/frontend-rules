#!/usr/bin/env python3
"""Copy or export frontend-rules and install the global Codex rule block."""

import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil


SOURCE = Path(__file__).resolve().parents[1]
RULES = ("rules/karpathy.md", "rules/frontend.md", "rules/components-and-theme.md")
FILES = (
    "README.md",
    "assets/readme-cover.png",
    *RULES,
    "docs/frontend-workflow.md",
    "docs/frontend-skills.md",
    "docs/project-map.md",
    "templates/MAP.md",
    "scripts/install.py",
)
# Keep the existing markers so installations of the Karpathy-only version are updated in place.
START = "<!-- frontend-rules:karpathy:start -->"
END = "<!-- frontend-rules:karpathy:end -->"


def read_rules(repo):
    return "\n\n".join((repo / relative).read_text(encoding="utf-8").strip() for relative in RULES) + "\n"


def merge_rule(current, rule):
    block = f"{START}\n{rule.rstrip()}\n{END}"
    if START not in current and END not in current:
        separator = "" if not current or current.endswith("\n\n") else "\n" if current.endswith("\n") else "\n\n"
        return current + separator + block + "\n"
    if current.count(START) != 1 or current.count(END) != 1:
        raise ValueError("Некорректные маркеры frontend-rules; файл оставлен без изменений.")
    start, end = current.index(START), current.index(END)
    if end < start:
        raise ValueError("Неверный порядок маркеров; файл оставлен без изменений.")
    return current[:start] + block + current[end + len(END):]


def install(repo, codex_home):
    if repo != SOURCE:
        if not (repo / ".git").exists():
            raise ValueError(f"Не найден Git-репозиторий: {repo}")
        for relative in FILES:
            target = repo / relative
            if target.exists() and target.read_bytes() != (SOURCE / relative).read_bytes():
                raise ValueError(f"Уже существует другой файл: {target}. Он оставлен без изменений.")
        for relative in FILES:
            target = repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                shutil.copyfile(SOURCE / relative, target)
        print(f"Файлы подготовлены: {repo}")

    override = codex_home / "AGENTS.override.md"
    target = override if override.is_file() and override.read_text(encoding="utf-8").strip() else codex_home / "AGENTS.md"
    current = target.read_text(encoding="utf-8") if target.exists() else ""
    updated = merge_rule(current, read_rules(repo))
    if updated != current:
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = target.with_name(f"{target.name}.backup-{stamp}")
            shutil.copyfile(target, backup)
            print(f"Резервная копия: {backup}")
        target.write_text(updated, encoding="utf-8")
        print(f"Codex: правила установлены в {target}")
    else:
        print(f"Codex: правила уже актуальны в {target}")
    print("Cursor: выполните python3 scripts/install.py --print-rules из корня репозитория и перенесите вывод в User Rules.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    operation = parser.add_mutually_exclusive_group()
    operation.add_argument("--repo", type=Path, default=SOURCE, help="Путь к клону frontend-rules")
    operation.add_argument("--print-rules", action="store_true", help="Вывести общий текст для Cursor User Rules")
    args = parser.parse_args()
    try:
        if args.print_rules:
            print(read_rules(SOURCE), end="")
        else:
            rules_codex_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
            install(args.repo.expanduser().resolve(), rules_codex_home)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Установка не завершена: {error}\n")
