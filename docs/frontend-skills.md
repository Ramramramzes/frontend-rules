# Навыки для этапов разработки

| Навык | Когда применять | Что проверить |
| --- | --- | --- |
| Figma Design to Code | На разборе задачи с макетом Figma, до реализации | Целевой фрейм, видимые вложенные узлы, состояния, компоненты, переменные и скриншот фрейма |
| Playwright CLI | После подключения логики и повторно после оформления | Пользовательский сценарий, клавиатура и фокус для изменённых элементов. При изменениях дизайна сверить скриншоты, адаптивность и темы |
| shadcn/ui | При оформлении, если в проекте нет подходящего компонента | Конфигурация, алиасы, библиотека примитивов, затронутые зависимости и файлы. Новый компонент использует тему проекта |

Playwright CLI используется для разовой проверки в браузере. Правила про ESLint, сборку, `typecheck` и написание новых тестов описаны в [frontend.md](../rules/frontend.md).

## Figma

Figma Design to Code входит в официальный плагин Figma. В Codex откройте **Plugins → Figma** и подключите аккаунт, если это ещё не сделано. В Cursor выполните `/add-plugin figma` в чате и авторизуйтесь. Для проверки попросите агента открыть конкретный фрейм по ссылке и показать его скриншот. [Подключение Figma MCP](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/).

## Playwright CLI и shadcn/ui

Выполните в терминале с Node.js 22.20 или новее. Если используете nvm и текущая версия ниже, сначала выполните `nvm install 22`.

```bash
npm install -g @playwright/cli@latest
playwright-cli install --skills=agents -g
npx skills add shadcn-ui/ui --skill shadcn --agent codex --global
```

Оба навыка устанавливаются в `~/.agents/skills/`, которую локально читают Codex и Cursor. Проверьте, что `playwright-cli --help` запускается и оба навыка видны в новой сессии. [Playwright CLI](https://playwright.dev/agent-cli/installation), [shadcn/ui](https://ui.shadcn.com/docs/skills), [каталоги навыков](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

Установка навыка shadcn/ui даёт агенту инструкции. Добавление конкретного компонента выполняется только в том проекте, где он нужен.
