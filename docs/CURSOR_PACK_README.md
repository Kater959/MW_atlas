# Metalwork Pulse · Cursor Pack

Это пакет для Cursor, чтобы собрать первый HTML-пилот Metalwork Pulse.

## Куда положить

Распакуй архив в папку проекта, например:

```text
/Users/nikolai/Documents/MW_atlas/
```

Должна получиться структура:

```text
MW_atlas/
  docs/
    locks/
      METALWORK_PULSE_CONTENT_MATRIX_PART_1_LOCK.md
      METALWORK_PULSE_CONTENT_MATRIX_PART_1_LOCK.pdf
    specs/
      DIR-01_CLAMPING_FIXTURES_HTML_SPEC.md
      DIR-01_CLAMPING_FIXTURES_HTML_SPEC.pdf
    prompts/
      CURSOR_TASK_CREATE_DIR_01_CLAMPING_HTML.md
  public/
    media/
      clamping/
        pneumatic/
          README_ASSETS.md
    models/
      clamping/
        pneumatic/
          README_MODELS.md
  src/
    html/
```

## Что есть что

```text
LOCK = смысл, тексты, боли, типы, кейсы, вопросы, CTA.
SPEC = конструкция интерфейса и поведение.
CURSOR TASK = готовая задача для Cursor.
```

## Что сделать в Cursor

1. Открой проект.
2. Открой файл:

```text
docs/prompts/CURSOR_TASK_CREATE_DIR_01_CLAMPING_HTML.md
```

3. Скопируй задачу в Cursor Chat.
4. Попроси создать:

```text
src/html/dir-01-clamping-fixtures.html
```

## Главное

Не разрешать Cursor делать лендинг.

Формула проекта:

```text
боль операции → точка потери управления → инженерное восстановление → render-card → gallery → 3D → case → questions → CTA
```
