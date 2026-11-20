# frontend-rules

![Марат за ноутбуком](assets/readme-cover.png)

Общая база правил и процедур для фронтенд-разработки.

## Содержимое

| Файл | Назначение |
| --- | --- |
| [rules/karpathy.md](rules/karpathy.md) | Четыре постоянно действующих принципа работы с кодом |
| [rules/frontend.md](rules/frontend.md) | Порядок работы, FSD, Effector, OpenAPI, асинхронность и проверки |
| [rules/components-and-theme.md](rules/components-and-theme.md) | Переиспользование компонентов, тема, адаптивность и доступность |
| [docs/frontend-workflow.md](docs/frontend-workflow.md) | Этапы разработки и критерии готовности |
| [docs/frontend-skills.md](docs/frontend-skills.md) | Подключение Figma, Playwright CLI и shadcn/ui |
| [docs/project-map.md](docs/project-map.md) | Карта проекта и навигация по коду |
| [templates/MAP.md](templates/MAP.md) | Шаблон карты для React и FSD |

Общие принципы Карпатого действуют для работы с кодом. Остальные правила относятся к фронтенд-задачам.

## Глобальное подключение

В Cursor откройте **Customize → Rules → User Rules** и вставьте текст трёх файлов из `rules/`. Если правила Карпатого уже добавлены из этой базы, замените их общим текстом. Остальные пользовательские правила сохраните.

## Обновление и проверка

После изменения файлов в `rules/` обновите текст правил в Codex и Cursor.

В новой сессии каждого инструмента проверьте два разных проекта: попросите назвать действующие общие принципы. В Codex можно дополнительно сверить текст в глобальном `AGENTS.md`. В Cursor проверьте сохранённый текст в User Rules. Это проверяет подключение; качество соблюдения правил оценивается по реальным изменениям и результатам проверок.

В `AGENTS.md` конкретного проекта указывайте его структуру, библиотеки, команды и ограничения.

## Источник и атрибуция

Правила перенесены из [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills), файл [CLAUDE.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), прочитанный 17 ноября 2026 года. Четыре принципа сохранены; адаптированы заголовок и Markdown-отступы. В README исходного проекта указана лицензия MIT.

Это составленные сообществом Karpathy-inspired guidelines на основе наблюдений Андрея Карпатого.

Документация интеграций: [Codex — AGENTS.md](https://developers.openai.com/codex/guides/agents-md/), [Cursor — Rules](https://cursor.com/docs/rules).
