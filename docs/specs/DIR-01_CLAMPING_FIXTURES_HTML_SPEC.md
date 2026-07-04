# DIR-01_CLAMPING_FIXTURES_HTML_SPEC

DIR-01_CLAMPING_FIXTURES_HTML_SPEC.md
STATUS
Этот файл является технической спецификацией первого HTML-пилота Metalwork Pulse.


SOURCE OF TRUTH
Основной источник содержания:



  METALWORK_PULSE_CONTENT_MATRIX_PART_1_LOCK.md


Все тексты, состояния, render-card, 3D placeholders, gallery placeholders и CTA для первого пилота
должны строиться от LOCK-документа Партии 1.


BASE RULE
Это не лендинг.
Это не презентация.
Это не каталог оборудования.
Это Metalwork Pulse diagnostic canvas для направления:



  DIR-01 · Станочная зажимная оснастка


Продуктовая рамка Metalwork Pulse: интерактивная инженерная система диагностики
производственных операций, которая находит место потери управления и возвращает процессу
ритм.




1. Назначение HTML-пилота
Первый HTML-пилот должен доказать механику всей будущей библиотеки Metalwork Pulse:



  direction → type navigator → active diagnostic dossier → render-card → gallery →
  3D model → case → questions → CTA


Пилотный файл:




                                                   1


  dir-01-clamping-fixtures.html


Пилотное направление:



  DIR-01 · Станочная зажимная оснастка


Активный тип по умолчанию:



  Пневматическая зажимная оснастка


Почему именно пневматика:



  Есть готовый визуальный эталон.
  Есть понятная боль: ручной зажим тормозит такт.
  Есть сильная инженерная логика: несколько действий → один управляемый сигнал.
  Есть нормальные callouts: цилиндр, прижим, база, распределитель.
  Есть понятные параметры: время зажима, давление, усилие, повторяемость.




2. Структура страницы
2.1. Общий layout desktop
Desktop должен собираться как инженерный diagnostic canvas, а не как обычная вертикальная
посадочная страница.


Базовая композиция:



  TOP HEADER
  └─ MAIN DIAGNOSTIC CANVAS
     ├─ LEFT EDITORIAL HERO
     ├─ CENTER TYPE NAVIGATOR / PULSE TREE
     └─ RIGHT DIAGNOSTIC DOSSIER
        ├─ Active type summary
        ├─ Pain / control loss / solution
        ├─ Render-card
        ├─ Gallery
        ├─ 3D model
        ├─ Case block
        ├─ Questions



                                               2


         ├─ Speaker notes
         └─ CTA


Этот подход соответствует базовой структуре Metalwork Pulse: слева editorial, по центру pulse tree,
справа diagnostic dossier.


2.2. Основные зоны страницы

Zone 01 · Pulse Header

Назначение: зафиксировать, что пользователь находится не на лендинге, а в инженерном diagnostic
canvas.


Содержит:



  METALWORK PULSE · ENGINEERING DIAGNOSTIC CANVAS
  DIR-01 · СТАНОЧНАЯ ЗАЖИМНАЯ ОСНАСТКА
  MW heartbeat line
  theme toggle


Zone 02 · Left Editorial Hero

Назначение: ударить в главную боль направления.


Содержит:



  kicker
  большой заголовок
  hook
  короткий diagnostic lead
  primary CTA


Zone 03 · Type Navigator

Назначение: переключать типы оснастки и менять dossier.


Типы:



  mechanical
  pneumatic
  hydraulic




                                                   3


  modular
  special


Zone 04 · Diagnostic Dossier

Назначение: показать выбранный тип как инженерную проблему, а не как товар.


Секции dossier:



  Название типа
  Сильный заголовок
  Короткий hook
  Боль клиента
  Где операция теряет управление
  Что делает инженерное решение
  Когда применять
  Когда не применять
  Данные для расчёта
  Вопросы менеджера
  Render-card
  Gallery
  3D model
  Case block
  Выгода
  Speaker notes
  CTA


Zone 05 · Render Fullscreen Viewer

Назначение: открыть render-card как инженерный экран.


Zone 06 · Gallery Fullscreen Viewer

Назначение: открыть фото / схему / деталь на весь экран с подписью и объяснением.


Zone 07 · Model Fullscreen Viewer

Назначение: открыть GLB-модель как инженерный объект, который можно крутить и понимать.


Zone 08 · Footer

Содержит:




                                               4


 MW PULSE · ENGINEERING DIAGNOSTIC CANVAS
 Показать проблемную операцию




3. Блоки интерфейса
3.1. Header
Обязательные элементы:



 Brand label:
 METALWORK PULSE


 System label:
 ENGINEERING DIAGNOSTIC CANVAS

 Direction label:
 DIR-01 · СТАНОЧНАЯ ЗАЖИМНАЯ ОСНАСТКА

 Theme toggle:
 DARK / LIGHT

 MW heartbeat line:
 inline SVG или image asset


Запрещено:



 обычный navbar как у SaaS
 пункты “О нас / Услуги / Контакты” в верхнем меню
 белая шапка
 синяя корпоративная палитра
 медицинская линия пульса с точками



3.2. Hero
Hero не должен продавать компанию. Он должен вскрывать боль операции.


Обязательные элементы:



 kicker
 headline




                                             5


  hook
  diagnostic lead
  CTA


Тексты hero см. раздел 13.


3.3. Type Navigator
Инженерный переключатель типов. Не табы в стиле SaaS.


Визуально:



  vertical pulse tree на desktop
  stacked diagnostic chips на tablet
  accordion/list на mobile


Каждый пункт должен показывать:



  ID
  название типа
  короткую strong phrase
  status indicator



3.4. Diagnostic Dossier
Правая панель. Главный рабочий экран.


Содержит не “описание услуги”, а разбор операции:



  Симптом
  Где теряется управление
  Инженерное восстановление
  Когда применять
  Когда не применять
  Что нужно для расчёта
  Вопросы клиенту
  Выгода




                                               6


3.5. Render-card block
Карточка должна выглядеть как часть Metalwork Pulse Diagnostic Render: near-black фон, инженерная
сетка, объект крупно, lime callouts, параметры, MW heartbeat line. Правила рендера: объект должен
быть читаемым, металл сатиновым, без black chrome-каши, без цветной CAD-раскраски.


3.6. Gallery block
Кликабельные фото / схемы / детали.


Каждый элемент gallery должен иметь:



  image
  caption
  что показано
  почему это важно клиенту
  type reference
  fullscreen action



3.7. 3D Model block
3D-модель не декор. Она доказывает, что объект можно рассмотреть, повернуть и понять. В
Metalwork Pulse model card должна иметь label GLB · 3D MODEL , fullscreen mode, rotate, zoom, reset
view и виды ISO / FRONT / TOP / SIDE.


3.8. Case block
Показывает не “пример проекта”, а инженерную причинно-следственную цепочку:



  Клиент обратился с проблемой
  Что было не так
  Какие данные запросили
  Как реализовали
  Какую боль закрыли



3.9. Speaker Notes
Скрытый / раскрываемый блок для менеджера.


Назначение:




                                                 7


  менеджер должен говорить через боль клиента,
  а не читать красивый текст с экрана.



3.10. CTA block
Главный CTA всегда:



  Показать проблемную операцию


Дополнительный supporting text:



  Покажите операцию, которую пора перестать терпеть — разберём, где она теряет
  управление и какой оснасткой закрыть риск.




4. Поведение type navigator
4.1. Типы в navigator
Пять типов:



  mechanical · Механическая
  pneumatic · Пневматическая
  hydraulic · Гидравлическая
  modular · Модульная
  special · Специальная



4.2. Default active
По умолчанию активен:



  pneumatic



4.3. При клике на тип
Cursor должен реализовать поведение:




                                         8


  1. снять active со всех type items;
  2. добавить active выбранному item;
  3. обновить diagnostic dossier;
  4. обновить render-card;
  5. обновить gallery;
  6. обновить model-viewer src;
  7. обновить case block;
  8. обновить questions;
  9. обновить speaker notes;
  10. сохранить выбранный тип в state;
  11. на mobile открыть / обновить bottom sheet dossier.



4.4. State model
Данные типов должны храниться в JS-структуре или JSON-подобном объекте внутри страницы.


Пример логики данных, не HTML-код:



  clampingTypes = {
    mechanical: {...},
    pneumatic: {...},
    hydraulic: {...},
    modular: {...},
    special: {...}
  }



4.5. Visual behavior
Active type:



  lime accent
  яркая линия pulse tree
  усиленный border
  видимый ID
  раскрытая краткая боль


Inactive type:



  muted text
  тонкий border




                                              9


  приглушённая линия
  без раскрытого dossier


Hover:



  может подсвечивать, но не должен быть обязательным действием


Focus:



  обязателен для keyboard navigation
  outline в accent color




5. Active state для пневматической оснастки
5.1. Active ID

  activeType = "pneumatic"



5.2. Active title

  Пневматическая зажимная оснастка



5.3. Active headline

  РУЧНОЙ ЗАЖИМ ТОРМОЗИТ ТАКТ.
  ПНЕВМАТИКА ПРЕВРАЩАЕТ ЕГО В СИГНАЛ.



5.4. Active hook

  Когда несколько ручных движений можно заменить одним управляемым действием,
  операция перестаёт ждать руки оператора.




                                         10


5.5. Active pain

 Оператор тратит время на зажимы, повторяет одно и то же движение, ошибается в
 последовательности, недожимает или пережимает. Станок стоит, такт плавает.



5.6. Active control loss

 В ручном зажиме, последовательности фиксации, синхронности точек и стабильности
 усилия.



5.7. Active engineering solution

 Переводит зажим в управляемый пневмосигнал, синхронизирует несколько точек,
 снижает ручные действия, делает последовательность установки повторяемой.



5.8. Active when to use

 При стабильной пневмосети, умеренных усилиях зажима, серийных деталях, коротком
 такте и повторяемых установках.



5.9. Active when not to use

 Когда нет стабильного воздуха, нужны очень большие усилия, среда убивает
 пневмокомпоненты или партия слишком мала для окупаемости.



5.10. Active calculation data

 Партия
 Такт
 Количество точек зажима
 Давление воздуха
 Усилия резания
 Зоны доступа инструмента
 Схема обработки
 Габариты детали
 Требования к деформации




                                        11


5.11. Active questions

 Есть ли стабильная пневмосеть?
 Сколько точек зажима?
 Сколько действий делает оператор?
 Какой такт нужен?
 Какие усилия резания?
 Где нельзя закрывать доступ инструменту?



5.12. Active render

 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-card-01.png



5.13. Active model

 /models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-01.glb



5.14. Active case

 Клиент обратился с проблемой:
 Оператор каждый цикл закручивает несколько прижимов. Деталь серийная, такт
 короткий, но установка съедает время.

 Как реализовали:
 Запросили схему обработки, количество зажимов, доступ инструмента и данные по
 пневмосети. Спроектировали пневмозажимы с управлением несколькими точками и
 понятной логикой установки.

 Выгода:
 Быстрее установка, меньше ручных действий, стабильнее последовательность, меньше
 зависимость от оператора.



5.15. Active speaker notes

 Пневматика нужна не для красоты. Она нужна там, где ручной зажим уже ворует
 такт. Оператор не должен каждый цикл изображать привод. Он ставит деталь, даёт
 сигнал, а оснастка сама закрывает нужные точки в нужной последовательности.
 Хороший оператор стоит дорого. Плохой оператор стоит ещё дороже. А операция,
 которая зависит от руки, каждый день выставляет счёт.




                                        12


6. Dark / Light theme
6.1. Default theme

  dark



6.2. Theme storage
Theme toggle должен:



  читать текущую тему из localStorage;
  если темы нет — ставить dark;
  записывать выбранную тему в localStorage;
  ставить data-theme на root element;
  обновлять label toggle.



6.3. Dark theme character

  near-black фон
  lime accent
  молочный текст
  тонкая инженерная сетка
  тёмный сатиновый металл
  ощущение закрытого командного экрана производства


Цветовая база dark:



  --bg: #050505
  --panel: #101010
  --elevated: #151515
  --text: #F2F0EA
  --muted: rgba(242,240,234,.52)
  --line: rgba(242,240,234,.10)
  --grid: rgba(242,240,234,.035)
  --accent: #B4FF2E
  --accent-soft: rgba(180,255,46,.18)




                                         13


6.4. Light theme character
Light theme не белая. Она должна выглядеть как:



  тёплая инженерная бумага
  CAD-сетка
  металл
  приглушённый lime
  премиальный техпресейл


Цветовая база light:



  --bg: #EEE7DA
  --bg-2: #E4D9C8
  --panel: #F7F1E6
  --elevated: #FFF9EF
  --text: #121212
  --muted: rgba(18,18,18,.58)
  --line: rgba(18,18,18,.12)
  --grid: rgba(18,18,18,.055)
  --accent: #72B900
  --accent-soft: rgba(114,185,0,.16)



6.5. Theme restrictions
Запрещено:



  чистый белый фон
  белый PowerPoint
  медицинский белый
  blue corporate IT
  пастельный SaaS




7. Fullscreen render viewer
7.1. Назначение
Render viewer открывает visual card на весь экран, чтобы менеджер мог показать её как инженерный
экран.




                                                  14


7.2. Trigger
Клик по render-card или кнопке:



  Открыть render



7.3. Содержимое fullscreen viewer

  image
  label: RENDER · CONCEPT VIEW
  title active type
  caption
  callouts list
  metrics list
  close button
  theme-aware background



7.4. Поведение

  openRenderViewer(typeId)
  closeRenderViewer()
  ESC закрывает viewer
  click outside закрывает viewer
  body scroll lock при открытии
  focus trap внутри viewer



7.5. Для пневматической оснастки
Render:



  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-card-01.png


Caption:



  Пневматическая оснастка превращает ручной зажим в управляемый сигнал и
  стабилизирует последовательность установки.


Callouts:




                                         15


  ПНЕВМОЦИЛИНДР
  ПРИЖИМНОЙ МЕХАНИЗМ
  КОРПУС ЗАЖИМА
  БАЗОВАЯ ПЛИТА
  ПНЕВМОРАСПРЕДЕЛИТЕЛЬ
  ОПОРНАЯ ТОЧКА


Metrics:



  ВРЕМЯ ЗАЖИМА
  ДАВЛЕНИЕ ПИТАНИЯ
  КОЛИЧЕСТВО КОНТУРОВ
  УСИЛИЕ ЗАЖИМА ПОСЛЕ РАСЧЁТА
  ПОВТОРЯЕМОСТЬ УСТАНОВКИ
  ТИП УПРАВЛЕНИЯ


Числа без реальных данных не обещать.




8. Fullscreen 3D model viewer
8.1. Назначение
3D viewer нужен не для декора. Он должен показать, что оснастка — инженерный объект, который
можно рассмотреть и понять.


8.2. Trigger
Клик по model-card или кнопке:



  Открыть 3D



8.3. Содержимое

  model-viewer
  label: GLB · 3D MODEL
  active type title
  node labels / callout overlay
  view controls




                                              16


  close button
  reset view



8.4. Controls
Обязательные controls:



  ISO
  FRONT
  TOP
  SIDE
  RESET
  ZOOM
  ROTATE



8.5. Model-viewer behavior

  camera-controls
  touch-action="pan-y"
  shadow-intensity около 0.8
  field-of-view около 35deg
  auto-rotate допустим, но должен отключаться при interaction



8.6. Для пневматической оснастки
Model path:



  /models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-01.glb


Mobile model fallback:



  /models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-mobile-01.glb


Draco compressed placeholder:



  /models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-draco-01.glb


Preview:




                                         17


  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-preview-01.png



8.7. 3D fallback
Если GLB ещё нет, показать placeholder:



  GLB · 3D MODEL PLACEHOLDER
  Модель будет подключена после подготовки CAD/GLB.


Нельзя скрывать блок. Placeholder нужен, чтобы архитектура пилота сразу была полной.




9. Gallery behavior
9.1. Назначение
Gallery показывает реальные фото, детали, узлы и схемы. Она не должна быть “галереей красивых
картинок”.


Каждая карточка отвечает на два вопроса:



  что показано?
  почему это важно клиенту?



9.2. Структура gallery item
Для каждого item:



  image path
  thumb path
  caption
  description
  client value
  typeId
  asset status: real / placeholder



9.3. Click behavior
При клике:




                                               18


  openGalleryViewer(index, typeId)
  открыть fullscreen
  показать image
  показать caption
  показать description
  показать client value
  показать prev / next



9.4. Keyboard behavior

  ESC закрывает
  ArrowLeft предыдущий
  ArrowRight следующий
  Tab не выходит за viewer



9.5. Пневматическая gallery placeholders
Использовать такие placeholders:



  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-gallery-01.jpg
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-gallery-01-thumb.jpg

  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-
  cylinder-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-clamp-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-base-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-valve-01.png


Captions:



  Общий вид пневмооснастки
  Пневмоцилиндр крупно
  Прижимной механизм
  Базовая плита
  Пневмораспределитель


Client value:



  показывает, где ручной зажим заменён управляемым узлом
  показывает источник управляемого движения
  показывает точку передачи усилия на деталь




                                         19


  показывает базу, где живёт повторяемость
  показывает управление несколькими зажимами




10. Mobile behavior
10.1. Mobile layout
Mobile — не ужатый desktop.


Структура:



  TOP HERO
  TYPE NAVIGATOR
  BOTTOM SHEET DIAGNOSTIC DOSSIER
  RENDER FULLSCREEN
  3D FULLSCREEN
  GALLERY FULLSCREEN
  CTA STICKY / SECTION CTA


Mobile-правила Metalwork Pulse: крупный hero, вертикальный список, dossier как bottom sheet, visual
и 3D открываются fullscreen, touch target минимум 44px, hover не обязательный.


10.2. Type navigator mobile
На mobile:



  type items идут вертикально;
  active item раскрыт;
  клик по inactive item меняет active type;
  после выбора открывается / обновляется bottom sheet dossier;
  не использовать мелкие tabs;
  минимальный touch target 44px.



10.3. Dossier mobile
Dossier должен работать как bottom sheet:



  collapsed state: title + hook + CTA
  expanded state: полный diagnostic dossier




                                                 20


  drag handle visual
  close / collapse


Если drag logic сложно, на первом пилоте допустимо:



  button: Развернуть dossier
  button: Свернуть dossier



10.4. Visual mobile
Render-card в основной ленте может быть компактным, но полноценно читается только в fullscreen.


Правило:



  не делать мелкие callouts единственным способом понять смысл.
  Под render-card всегда должна быть текстовая расшифровка callouts.



10.5. 3D mobile

  model-viewer открывается fullscreen;
  touch rotate включён;
  zoom pinch включён;
  кнопки ISO / FRONT / TOP / SIDE крупные;
  если модель тяжёлая — использовать mobile GLB fallback.




11. Какие данные брать из матрицы
11.1. Для каждого типа брать
Из LOCK-документа брать поля:



  Название типа
  Сильный заголовок
  Короткий hook
  Боль клиента
  Где операция теряет управление
  Что делает инженерное решение
  Когда применять
  Когда не применять




                                               21


 Данные для расчёта
 Вопросы менеджера
 Render-card
 Callouts
 Параметры visual card
 Фото/галерея
 3D-модель
 Пример запроса заказчика
 Как реализовали
 Выгода для клиента
 Речь спикера
 CTA



11.2. Типы DIR-01

 mechanical
 pneumatic
 hydraulic
 modular
 special



11.3. Mapping типа в UI

mechanical


 Механическая зажимная оснастка
 ПРОСТАЯ ОСНАСТКА НЕ ПРОЩАЕТ ХАОС.
 ОНА ЕГО НЕ ПУСКАЕТ В ОПЕРАЦИЮ.


pneumatic


 Пневматическая зажимная оснастка
 РУЧНОЙ ЗАЖИМ ТОРМОЗИТ ТАКТ.
 ПНЕВМАТИКА ПРЕВРАЩАЕТ ЕГО В СИГНАЛ.


hydraulic


 Гидравлическая зажимная оснастка
 КОГДА ЦЕНА ОШИБКИ ВЫСОКА,
 УСИЛИЕ НЕ ДОЛЖНО БЫТЬ “НА ОЩУЩЕНИЯХ”.




                                         22


modular


  Модульная зажимная оснастка
  ДЕТАЛИ МЕНЯЮТСЯ.
  ХАОС ПЕРЕНАЛАДКИ — НЕТ.


special


  Специальная зажимная оснастка
  ЕСЛИ ОПЕРАЦИЯ ПОВТОРЯЕТСЯ,
  ХВАТИТ КАЖДЫЙ РАЗ РЕШАТЬ ЕЁ РУКАМИ.




12. Какие assets подключать
Asset naming должен соблюдать правило: один визуал — одно понятное имя, без
 final_final_2.png , photo123.png , новое.png , рендер_красивый.png .


12.1. Common assets

  public/media/pulse/common/mw-pulse-heartbeat-line-clean-01.svg
  public/media/pulse/common/mw-pulse-bg-grid-dark-01.png
  public/media/pulse/common/mw-pulse-bg-grid-light-01.png



12.2. Direction assets

  public/media/clamping/mw-pulse-clamping-hero-01.png
  public/media/clamping/mw-pulse-clamping-callouts-01.png
  public/media/clamping/mw-pulse-clamping-before-after-01.png
  public/media/clamping/mw-pulse-clamping-anatomy-01.png



12.3. Pneumatic assets

  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-hero-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-callouts-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-wide-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-card-01.png
  public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-
  cylinder-01.png




                                              23


 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-clamp-01.png
 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-base-01.png
 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-detail-valve-01.png
 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-light-01.png
 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-dark-01.png
 public/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-preview-01.png



12.4. Mechanical assets

 public/media/clamping/mechanical/mw-pulse-clamping-mechanical-card-01.png
 public/media/clamping/mechanical/mw-pulse-clamping-mechanical-hero-01.png
 public/media/clamping/mechanical/mw-pulse-clamping-mechanical-callouts-01.png
 public/media/clamping/mechanical/mw-pulse-clamping-mechanical-detail-
 handle-01.png
 public/media/clamping/mechanical/mw-pulse-clamping-mechanical-detail-
 screw-01.png
 public/media/clamping/mechanical/mw-pulse-clamping-mechanical-model-
 preview-01.png



12.5. Hydraulic assets

 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-card-01.png
 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-hero-01.png
 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-callouts-01.png
 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-wide-01.png
 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-detail-
 cylinder-01.png
 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-detail-
 powerpack-01.png
 public/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-model-preview-01.png



12.6. Modular assets

 public/media/clamping/modular/mw-pulse-clamping-modular-card-01.png
 public/media/clamping/modular/mw-pulse-clamping-modular-hero-01.png
 public/media/clamping/modular/mw-pulse-clamping-modular-callouts-01.png
 public/media/clamping/modular/mw-pulse-clamping-modular-detail-grid-plate-01.png
 public/media/clamping/modular/mw-pulse-clamping-modular-detail-clamp-01.png
 public/media/clamping/modular/mw-pulse-clamping-modular-model-preview-01.png




                                        24


12.7. Special assets
В asset naming list направление называется custom , но в UI допускается русский термин
специальная оснастка .


Использовать paths:



  public/media/clamping/custom/mw-pulse-clamping-custom-card-01.png
  public/media/clamping/custom/mw-pulse-clamping-custom-hero-01.png
  public/media/clamping/custom/mw-pulse-clamping-custom-callouts-01.png
  public/media/clamping/custom/mw-pulse-clamping-custom-detail-base-01.png
  public/media/clamping/custom/mw-pulse-clamping-custom-detail-control-01.png
  public/media/clamping/custom/mw-pulse-clamping-custom-model-preview-01.png



12.8. Models

  public/models/clamping/mw-pulse-clamping-model-01.glb

  public/models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-01.glb
  public/models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-mobile-01.glb
  public/models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-draco-01.glb

  public/models/clamping/mechanical/mw-pulse-clamping-mechanical-model-01.glb
  public/models/clamping/hydraulic/mw-pulse-clamping-hydraulic-model-01.glb
  public/models/clamping/modular/mw-pulse-clamping-modular-model-01.glb
  public/models/clamping/custom/mw-pulse-clamping-custom-model-01.glb




13. Какие placeholders использовать
13.1. Image placeholder rule
Если asset ещё не готов, блок не удалять.


Показывать placeholder:



  RENDER PLACEHOLDER
  Файл ожидается:
  [path]




                                               25


13.2. Model placeholder rule
Если GLB ещё нет:



  GLB · 3D MODEL PLACEHOLDER
  Модель будет подключена после подготовки CAD/GLB.



13.3. Gallery placeholder rule
Если фото ещё нет:



  PHOTO PLACEHOLDER
  Нужно фото:
  [что именно]
  Почему важно:
  [производственная ценность]



13.4. Pneumatic placeholder priority
Для пилота пневматики первым подключать:



  mw-pulse-clamping-pneumatic-card-01.png
  mw-pulse-clamping-pneumatic-callouts-01.png
  mw-pulse-clamping-pneumatic-model-preview-01.png
  mw-pulse-clamping-pneumatic-model-01.glb


Если реального файла нет, показывать placeholder с тем же именем.




14. Тексты hero
14.1. Header label

  METALWORK PULSE · ENGINEERING DIAGNOSTIC CANVAS



14.2. Direction label

  DIR-01 · СТАНОЧНАЯ ЗАЖИМНАЯ ОСНАСТКА




                                               26


14.3. Hero kicker

  RECOVERY MODULE · CLAMPING FIXTURES


Допустима RU-версия:



  МОДУЛЬ ВОССТАНОВЛЕНИЯ · ЗАЖИМНАЯ ОСНАСТКА


Так как проект RU-first, основной экран должен показывать русскую версию.


14.4. Hero headline

  СТАНОК ЗА МИЛЛИОНЫ БЕССИЛЕН,
  ЕСЛИ БАЗА ДЕРЖИТСЯ НА ОЩУЩЕНИЯХ.



14.5. Hero hook

  Если деталь физически можно поставить криво — рано или поздно её поставят криво.



14.6. Hero diagnostic lead

  Станочная зажимная оснастка убирает неопределённость установки до первого реза:
  задаёт базу, упор, зажим и делает правильное положение детали единственным
  рабочим вариантом.



14.7. Hero pain bullets

  ручная выверка на каждой партии
  подкладки и перезажим
  риск перекоса и смещения детали
  зависимость результата от смены и оператора
  нестабильное время установки
  прижим “по ощущениям”




                                               27


14.8. Primary CTA

  Показать проблемную операцию



14.9. CTA support

  Покажите операцию, которую пора перестать терпеть — разберём, где она теряет
  управление и какой оснасткой закрыть риск.




15. Обязательные sections
Cursor должен собрать страницу с этими section IDs / логическими блоками.


15.1. Required sections

  pulse-header
  direction-hero
  type-navigator
  diagnostic-dossier
  control-loss-section
  engineering-solution-section
  when-to-use-section
  when-not-to-use-section
  calculation-data-section
  questions-section
  render-card-section
  gallery-section
  model-card-section
  case-section
  benefit-section
  speaker-notes-section
  cta-section
  visual-fullscreen-viewer
  gallery-fullscreen-viewer
  model-fullscreen-viewer
  pulse-footer



15.2. Нельзя удалять sections
Даже если asset ещё не готов:




                                               28


  render-card-section остаётся с placeholder
  gallery-section остаётся с placeholder
  model-card-section остаётся с placeholder



15.3. Sections order
Desktop order внутри dossier:



  01 Active type intro
  02 Pain
  03 Control loss
  04 Engineering solution
  05 Render-card
  06 Gallery
  07 3D model
  08 When to use / When not to use
  09 Calculation data
  10 Questions
  11 Case
  12 Benefit
  13 Speaker notes
  14 CTA


Mobile order:



  01 Hero
  02 Type navigator
  03 Active type short dossier
  04 CTA
  05 Render-card
  06 Gallery
  07 3D model
  08 Full diagnostic details
  09 Case
  10 Questions
  11 Speaker notes
  12 CTA repeat




16. JS-функции
HTML-код пока не писать, но Cursor должен заложить следующие функции.




                                             29


16.1. Theme

 initTheme()
 setTheme(theme)
 toggleTheme()
 getStoredTheme()
 applyTheme(theme)



16.2. Type state

 initTypeNavigator()
 setActiveType(typeId)
 renderTypeNavigator()
 renderDiagnosticDossier(typeId)
 renderRenderCard(typeId)
 renderGallery(typeId)
 renderModelCard(typeId)
 renderCaseBlock(typeId)
 renderQuestions(typeId)
 renderSpeakerNotes(typeId)



16.3. Render viewer

 openRenderViewer(typeId)
 closeRenderViewer()
 bindRenderViewerEvents()



16.4. Gallery viewer

 openGalleryViewer(typeId, index)
 closeGalleryViewer()
 showNextGalleryItem()
 showPrevGalleryItem()
 renderGalleryViewerItem(typeId, index)



16.5. Model viewer

 openModelViewer(typeId)
 closeModelViewer()
 setModelView(viewName)




                                          30


  resetModelView()
  useMobileModelIfNeeded(typeId)


View names:



  iso
  front
  top
  side



16.6. Mobile dossier

  initMobileDossier()
  openMobileDossier(typeId)
  closeMobileDossier()
  toggleMobileDossier()
  syncMobileDossierWithActiveType(typeId)



16.7. Accessibility / keyboard

  handleEscapeKey()
  trapFocus(modalId)
  releaseFocus()
  handleArrowNavigation()
  setAriaExpanded(element, state)
  setAriaSelected(element, state)



16.8. Body lock

  lockBodyScroll()
  unlockBodyScroll()



16.9. Init

  initPulsePilot()


Init order:




                                            31


  initTheme()
  initTypeNavigator()
  setActiveType("pneumatic")
  initMobileDossier()
  bindRenderViewerEvents()
  bindGalleryViewerEvents()
  bindModelViewerEvents()
  bindKeyboardEvents()




17. Data model для Cursor
Cursor должен создать единый объект данных для DIR-01.


17.1. Direction object

  directionId: "DIR-01"
  slug: "clamping-fixtures"
  title: "Станочная зажимная оснастка"
  headline: "СТАНОК ЗА МИЛЛИОНЫ БЕССИЛЕН, ЕСЛИ БАЗА ДЕРЖИТСЯ НА ОЩУЩЕНИЯХ."
  hook: "Если деталь физически можно поставить криво — рано или поздно её поставят
  криво."
  cta: "Показать проблемную операцию"
  activeTypeDefault: "pneumatic"



17.2. Type object fields
Каждый тип должен иметь поля:



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
  calculationData[]
  questions[]
  renderCard




                                              32


  renderCaption
  callouts[]
  metrics[]
  gallery[]
  model
  caseRequest
  caseImplementation
  benefit
  speakerNotes
  cta



17.3. Gallery object fields

  src
  thumb
  caption
  description
  clientValue
  status



17.4. Model object fields

  src
  mobileSrc
  dracoSrc
  preview
  label
  nodes[]




18. Как не превратить это в лендинг
18.1. Запрещённые паттерны
Не делать:



  hero на весь экран с одной красивой фразой
  три карточки преимуществ
  “наши услуги”
  “почему выбирают нас”
  “оставьте заявку”




                                         33


  абстрактные иконки
  улыбающиеся люди в касках
  стоковые фото цеха
  корпоративный синий
  SaaS cards
  белый PowerPoint
  medical vibe
  cyberpunk HUD
  цветной CAD как финальный render
  black chrome, где объект слился в кашу



18.2. Обязательная логика каждого экрана
Каждый экран должен отвечать:



  какая боль в операции?
  где теряется управление?
  какой физический элемент возвращает контроль?
  что должен увидеть клиент на render-card?
  какие данные нужны для расчёта?
  что спросить у клиента?



18.3. Правильный критерий
Клиент не должен думать:



  Красиво.


Клиент должен думать:



  Блядь, это же про наш участок.



18.4. Copywriting rules
Писать:



  коротко
  жёстко
  через операцию




                                           34


  через брак, такт, базу, усилие, повторяемость
  через деньги, которые уходят в простои, переделки и ручную подгонку


Не писать:



  мы динамично развиваемся
  комплексные решения
  индивидуальный подход
  инновации и качество
  повышаем эффективность
  лучшие на рынке



18.5. Strong phrases allowed and required
Использовать без смягчения:



  Хорошая оснастка не помогает ошибаться меньше. Она не оставляет ошибке места.
  Если деталь физически можно поставить криво — рано или поздно её поставят криво.
  Мы не продаём железо. Мы проектируем физический запрет на ошибку.
  Хороший оператор стоит дорого. Плохой оператор стоит ещё дороже.
  Героизм в цеху — симптом операции, которую пора перепроектировать.




19. Acceptance criteria
Пилот считается собранным правильно, если:



  1. По умолчанию открыт тип “Пневматическая зажимная оснастка”.
  2. Type navigator переключает все пять типов.
  3. Diagnostic dossier обновляется без перезагрузки страницы.
  4. Dark theme включена по умолчанию.
  5. Light theme тёплая, не белая.
  6. Render-card открывается fullscreen.
  7. Gallery открывается fullscreen и листается.
  8. Model-viewer открывается fullscreen.
  9. Есть controls ISO / FRONT / TOP / SIDE / RESET.
  10. На mobile dossier работает как bottom sheet или раскрываемый блок.
  11. Все assets имеют правильные имена или placeholders.
  12. CTA везде один: “Показать проблемную операцию”.
  13. Нет SaaS-лендинга.
  14. Нет PowerPoint-вайба.
  15. Нет medical.




                                             35


 16. Нет cyberpunk.
 17. Нет цветного CAD.
 18. Нет black chrome-каши.
 19. Каждый блок объясняет производственную боль.
 20. Клиент узнаёт свой участок.




20. Что Cursor должен сделать после этой
спецификации
Следующий файл после этой спецификации:



 dir-01-clamping-fixtures.html


Перед написанием HTML Cursor должен:



 1. Создать data object для всех пяти типов DIR-01.
 2. Заложить CSS variables для dark/light.
 3. Заложить component structure.
 4. Заложить JS state для activeType.
 5. Подготовить placeholders для отсутствующих assets.
 6. Проверить mobile behavior.
 7. Не добавлять лендинговые блоки.




NEXT STEP
Следующий файл:



 dir-01-clamping-fixtures.html




                                          36


