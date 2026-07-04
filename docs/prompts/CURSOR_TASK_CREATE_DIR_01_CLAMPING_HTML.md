# CURSOR_TASK_CREATE_DIR_01_CLAMPING_HTML.md

## Задача

Создай первый рабочий HTML-файл:

```text
src/html/dir-01-clamping-fixtures.html
```

## Источники правды

Используй строго эти документы:

```text
docs/locks/METALWORK_PULSE_CONTENT_MATRIX_PART_1_LOCK.md
docs/specs/DIR-01_CLAMPING_FIXTURES_HTML_SPEC.md
```

PDF-версии лежат рядом как архивные копии.

## Главное правило

Это не лендинг.  
Это не презентация.  
Это не каталог оборудования.  
Это **Metalwork Pulse diagnostic canvas**.

## Что нужно сделать

Один самодостаточный HTML-файл:

- inline CSS;
- inline JS;
- dark theme по умолчанию;
- light theme тёплая, не белая;
- `data-theme` + `localStorage`;
- desktop layout: `LEFT editorial / CENTER type navigator / RIGHT diagnostic dossier`;
- mobile layout: `TOP hero / type list / expandable dossier / fullscreen visual / fullscreen 3D`;
- active type по умолчанию: `pneumatic`;
- переключение всех 5 типов без перезагрузки:
  - mechanical;
  - pneumatic;
  - hydraulic;
  - modular;
  - special;
- render-card fullscreen viewer;
- gallery fullscreen viewer с prev/next;
- model-viewer card;
- fullscreen model viewer;
- controls: ISO / FRONT / TOP / SIDE / RESET;
- placeholders для отсутствующих assets;
- CTA: `Показать проблемную операцию`;
- speaker notes;
- без внешних зависимостей, кроме `model-viewer`.

## Данные

Все тексты для пяти типов брать из:

```text
docs/locks/METALWORK_PULSE_CONTENT_MATRIX_PART_1_LOCK.md
```

Техническое поведение брать из:

```text
docs/specs/DIR-01_CLAMPING_FIXTURES_HTML_SPEC.md
```

## В JS-объекте для каждого типа должны быть поля

```text
id
title
shortTitle
headline
hook
pain
controlLoss
engineeringSolution
whenUse
whenNotUse
calculationData
questions
renderCard
renderCaption
callouts
metrics
gallery
model
caseRequest
caseImplementation
benefit
speakerNotes
cta
```

## Asset fallback

Если asset не существует — показывать premium placeholder с именем ожидаемого файла.  
Не показывать битые картинки.

## Запрещено

- SaaS-лендинг;
- белый PowerPoint;
- medical;
- cyberpunk;
- цветной CAD как финальный render;
- black chrome-каша;
- корпоративная вода;
- “О нас / Услуги / Контакты” navbar;
- “почему выбирают нас”;
- “динамично развиваемся”.

## Acceptance check

После генерации проверь:

1. По умолчанию открыт тип `Пневматическая зажимная оснастка`.
2. Все 5 типов переключаются.
3. Dossier обновляется без перезагрузки.
4. Dark theme включена по умолчанию.
5. Light theme тёплая, не белая.
6. Render-card открывается fullscreen.
7. Gallery открывается fullscreen и листается.
8. Model-viewer открывается fullscreen.
9. Есть controls ISO / FRONT / TOP / SIDE / RESET.
10. Mobile не является ужатым desktop.
11. CTA везде один: `Показать проблемную операцию`.
12. Нет лендингового вайба.
13. Каждый блок объясняет производственную боль.
