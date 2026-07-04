#!/usr/bin/env python3
"""Build DIR-01 clamping fixtures diagnostic HTML from LOCK content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTS = [
    ROOT / "src/html/dir-01-clamping-fixtures.html",
    ROOT / "public/html/dir-01-clamping-fixtures.html",
]

# Paths are absolute from site root (serve via /html/... or Next public/)
TYPES_JS = r"""
const TYPES = [
  {
    id: "mechanical",
    title: "Механическая зажимная оснастка",
    shortTitle: "Механическая",
    headline: ["ПРОСТАЯ ОСНАСТКА НЕ ПРОЩАЕТ ХАОС.", "ОНА ЕГО НЕ ПУСКАЕТ В ОПЕРАЦИЮ."],
    hook: "Когда операция не требует автоматики, ей всё равно нужна жёсткая база, понятный упор и зажим без гадания рукой.",
    pain: "Деталь выставляют вручную, подкладывают, поправляют, перезажимают. Один оператор делает нормально, другой ловит базу полсмены. Станок ждёт, резание ещё не началось, а деньги уже горят.",
    controlLoss: "В базировании, упоре, последовательности зажима и повторяемости установки. Деталь физически может занять несколько положений — значит одно из них однажды станет браком.",
    engineeringSolution: "Задаёт однозначные базы, механические упоры, прижимные точки, защиту от смещения и понятную последовательность установки.",
    whenUse: "Когда нужна надёжная ремонтопригодная оснастка без сложной пневматики или гидравлики. Для серийных и мелкосерийных деталей, где проблема в установке, а не в резании.",
    whenNotUse: "Когда зажимов много и ручное действие само становится потерей такта. Когда нужны высокие усилия или синхронный зажим нескольких точек.",
    calculationData: "Чертёж детали, 3D-модель, схема обработки, допуски на базы, припуски, тип станка, стол, доступ инструмента, усилия резания, партия, такт.",
    questions: ["Сколько времени уходит на установку?","Где оператор поправляет деталь рукой?","Какие размеры уходят?","Есть ли перезажим?","Как меняется результат при смене оператора?","Где деталь может физически встать неправильно?"],
    renderCard: "/media/clamping/mechanical/mw-pulse-clamping-mechanical-card-01.png",
    renderCaption: "Механическая зажимная оснастка · render · concept view",
    renderPhoto: "/media/clamping/mechanical/mw-pulse-clamping-mechanical-live-shop.jpg?v=5",
    photoCaption: "Механическая оснастка · живое фото в цеху",
    // Подложки текстовых шагов (ключи = step.key, не slug)
    stepBackgrounds: {
      hook: "/media/pulse-bg/hook-screen.png",
      pain: "/media/clamping/mechanical/mw-pulse-clamping-mechanical-live-shop.jpg?v=5",
      loss: "/media/pulse-bg/bg-01.png",
      fix: "/media/clamping/mechanical/mw-pulse-clamping-mechanical-card-01.png",
      benefit: "/media/clamping/mechanical/mw-pulse-clamping-mechanical-live-shop.jpg?v=5",
      cta: "/media/pulse-bg/hook-screen.png",
    },
    callouts: [
      ["БАЗИРУЮЩИЙ УПОР","Задаёт положение детали"],
      ["КОРПУС ОСНАСТКИ","Жёсткая несущая система"],
      ["БОКОВОЙ УПОР","Не даёт детали уйти"],
      ["ПАЛЕЦ ФИКСАЦИИ","Однозначная ориентация"],
      ["БАЗОВАЯ ПЛИТА","Собирает операцию в систему"],
      ["ПРИЖИМНОЙ ЭЛЕМЕНТ","Удерживает с понятным усилием"],
      ["ОПОРНАЯ ПОВЕРХНОСТЬ","Убирает прогиб и вибрацию"]
    ],
    metrics: [
      ["Тип оснастки","Механическая станочная"],
      ["Тип зажима","Рычажный / эксцентрик"],
      ["Повторяемость","±0.01 мм по базам"],
      ["Жёсткость","Высокая, без пневмо/гидро"],
      ["Время установки","5–10 сек быстрая фиксация"],
      ["Ресурс",">1 000 000 циклов"]
    ],
    gallery: [
      {src:"/media/clamping/mechanical/mw-pulse-clamping-mechanical-live-shop.jpg?v=5",caption:"Оснастка в цеху",value:"Реальная установка на участке"},
      {src:"/media/clamping/mechanical/mw-pulse-clamping-mechanical-card-01.png",caption:"Render · concept view",value:"Инженерная visual card"}
    ],
    model: {
      src:"/models/clamping/mechanical/mw-pulse-clamping-mechanical-model-01.glb",
      poster:"/media/clamping/mechanical/mw-pulse-clamping-mechanical-model-preview-01.png"
    },
    caseRequest: "Деталь небольшая, но каждый раз выставляем долго. Оператор подкладывает пластинки, ловит положение индикатором, потом всё равно есть разброс.",
    caseImplementation: "Запросили чертёж, допуски, схему обработки и фото текущей установки. Развели базы, задали два жёстких упора, добавили механические прижимы и ограничили неправильную ориентацию детали.",
    benefit: "Меньше ручной выверки, меньше зависимость от смены, понятнее установка, меньше риск смещения до первого реза.",
    speakerNotes: "Механическая оснастка — это не «простая железка». Это физический способ запретить детали вставать как попало. Здесь не оператор каждый раз убеждает заготовку занять правильное положение. База, упор и зажим уже задали ей единственный нормальный сценарий. Хорошая оснастка не помогает ошибаться меньше. Она не оставляет ошибке места.",
    cta: "Показать проблемную операцию"
  },
  {
    id: "pneumatic",
    title: "Пневматическая зажимная оснастка",
    shortTitle: "Пневматическая",
    headline: ["РУЧНОЙ ЗАЖИМ ТОРМОЗИТ ТАКТ.", "ПНЕВМАТИКА ПРЕВРАЩАЕТ ЕГО В СИГНАЛ."],
    hook: "Когда несколько ручных движений можно заменить одним управляемым действием, операция перестаёт ждать руки оператора.",
    pain: "Оператор тратит время на зажимы, повторяет одно и то же движение, ошибается в последовательности, недожимает или пережимает. Станок стоит, такт плавает.",
    controlLoss: "В ручном зажиме, последовательности фиксации, синхронности точек и стабильности усилия.",
    engineeringSolution: "Переводит зажим в управляемый пневмосигнал, синхронизирует несколько точек, снижает ручные действия, делает последовательность установки повторяемой.",
    whenUse: "При стабильной пневмосети, умеренных усилиях зажима, серийных деталях, коротком такте и повторяемых установках.",
    whenNotUse: "Когда нет стабильного воздуха, нужны очень большие усилия, среда убивает пневмокомпоненты или партия слишком мала для окупаемости.",
    calculationData: "Партия, такт, количество точек зажима, давление воздуха, усилия резания, зоны доступа инструмента, схема обработки, габариты детали, требования к деформации.",
    questions: ["Есть ли стабильная пневмосеть?","Сколько точек зажима?","Сколько действий делает оператор?","Какой такт нужен?","Какие усилия резания?","Где нельзя закрывать доступ инструменту?"],
    renderCard: "/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-card-01.png",
    renderCaption: "Пневматическая зажимная оснастка · concept view",
    renderPhoto: "/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-live-shop.jpg?v=1",
    photoCaption: "Пневматическая оснастка · живое фото в станке",
    stepBackgrounds: {
      hook: "/media/pulse-bg/hook-screen.png",
      pain: "/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-live-shop.jpg?v=1",
      loss: "/media/pulse-bg/bg-02.png",
      fix: "/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-card-01.png",
      benefit: "/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-live-shop.jpg?v=1",
      cta: "/media/pulse-bg/hook-screen.png",
    },
    callouts: [["ПНЕВМОЦИЛИНДР","Двустороннего действия"],["ПРИЖИМНОЙ МЕХАНИЗМ","Рычажный привод"],["КОРПУС ЗАЖИМА","Закалённая сталь"],["БАЗОВАЯ ПЛИТА","Инструментальная сталь"],["ПНЕВМОРАСПРЕДЕЛИТЕЛЬ","Управление каждым модулем"],["ОПОРНАЯ ТОЧКА","Повторяемая база"]],
    metrics: [["Clamping Time","1.2 sec"],["Clamping Force","up to 25 kN"],["Supply Pressure","0.6 MPa"],["Repeatability","±0.01 mm"]],
    gallery: [
      {src:"/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-live-shop.jpg?v=1",caption:"Пневмооснастка в станке",value:"Живое фото установки"},
      {src:"/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-card-01.png",caption:"Render · concept view",value:"Инженерная visual card"}
    ],
    model: {src:"/models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-01.glb",poster:"/media/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-preview-01.png",mobileSrc:"/models/clamping/pneumatic/mw-pulse-clamping-pneumatic-model-mobile-01.glb"},
    caseRequest: "Оператор каждый цикл закручивает несколько прижимов. Деталь серийная, такт короткий, но установка съедает время.",
    caseImplementation: "Запросили схему обработки, количество зажимов, доступ инструмента и данные по пневмосети. Спроектировали пневмозажимы с управлением несколькими точками и понятной логикой установки.",
    benefit: "Быстрее установка, меньше ручных действий, стабильнее последовательность, меньше зависимость от оператора.",
    speakerNotes: "Пневматика нужна не для красоты. Она нужна там, где ручной зажим уже ворует такт. Оператор не должен каждый цикл изображать привод. Он ставит деталь, даёт сигнал, а оснастка сама закрывает нужные точки в нужной последовательности. Хороший оператор стоит дорого. Плохой оператор стоит ещё дороже. А операция, которая зависит от руки, каждый день выставляет счёт.",
    cta: "Показать проблемную операцию"
  },
  {
    id: "hydraulic",
    title: "Гидравлическая зажимная оснастка",
    shortTitle: "Гидравлическая",
    headline: ["КОГДА ЦЕНА ОШИБКИ ВЫСОКА,", "УСИЛИЕ НЕ ДОЛЖНО БЫТЬ «НА ОЩУЩЕНИЯХ»."],
    hook: "Если деталь тяжёлая, резание серьёзное, а смещение дорогое — усилие зажима должно быть рассчитанным, а не героическим.",
    pain: "Деталь уводит под нагрузкой, ручной зажим не держит стабильно, оператор боится деформировать заготовку или, наоборот, недожимает. Ошибка проявляется уже после обработки.",
    controlLoss: "В усилии зажима, деформации детали, устойчивости под резанием и контроле силового контура.",
    engineeringSolution: "Задаёт управляемое гидравлическое усилие, распределяет точки зажима, снижает риск смещения и фиксирует деталь под нагрузкой.",
    whenUse: "При больших усилиях резания, тяжёлых деталях, ответственных операциях, серийной обработке, где цена смещения выше стоимости оснастки.",
    whenNotUse: "Когда усилия умеренные и достаточно механики/пневматики. Когда нет условий для гидравлики или обслуживание усложнит процесс сильнее, чем решит проблему.",
    calculationData: "Усилия резания, материал детали, геометрия, жёсткость, зоны деформации, допуски, партия, схема обработки, доступ инструмента, требования по безопасности.",
    questions: ["Были ли смещения детали?","Какие припуски и силы резания?","Есть ли следы деформации после зажима?","Какие размеры критичны?","Как сейчас контролируют усилие?"],
    renderCard: "/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-card-01.png?v=1",
    renderCaption: "Многоместный гидрозажим · render · concept view",
    renderPhoto: "/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-live-shop.jpg?v=1",
    photoCaption: "Многоместный гидрозажим · живое фото",
    stepBackgrounds: {
      hook: "/media/pulse-bg/hook-screen.png",
      pain: "/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-live-shop.jpg?v=1",
      loss: "/media/pulse-bg/bg-03.png",
      fix: "/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-card-01.png?v=1",
      benefit: "/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-live-shop.jpg?v=1",
      cta: "/media/pulse-bg/hook-screen.png",
    },
    callouts: [
      ["ГИДРОЦИЛИНДРЫ","Управляемое усилие зажима"],
      ["ПРИЖИМНЫЕ РЫЧАГИ","Фиксация без ручной дотяжки"],
      ["ГИДРОЛИНИЯ","Питание модулей зажима"],
      ["БАЗОВАЯ ПЛИТА","Жёсткая геометрия установки"],
      ["ОПОРНЫЕ ТОЧКИ","Деталь остаётся в позиции"]
    ],
    metrics: [
      ["Усилие зажима","до 80 kN"],
      ["Позиций","6–8"],
      ["Давление","до 16 MPa"],
      ["Повторяемость","±0.01 mm"]
    ],
    gallery: [
      {src:"/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-live-shop.jpg?v=1",caption:"Гидрозажим в цеху",value:"Живое фото установки"},
      {src:"/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-card-01.png?v=1",caption:"Многоместный гидрозажим",value:"Одно давление — одинаковая фиксация группы"}
    ],
    model: {
      src:"/models/clamping/hydraulic/mw-pulse-clamping-hydraulic-model-01.glb?v=1",
      poster:"/media/clamping/hydraulic/mw-pulse-clamping-hydraulic-model-preview-01.png?v=1"
    },
    caseRequest: "На тяжёлой детали при обработке появляется смещение. Зажимают сильнее — появляется риск деформации.",
    caseImplementation: "Собрали данные по усилиям резания, геометрии детали и критичным размерам. Разнесли опоры, рассчитали точки гидрозажима, заложили контроль давления и доступ инструмента.",
    benefit: "Управляемое усилие, ниже риск смещения, понятнее силовой контур, меньше зависимость от «чувства» оператора.",
    speakerNotes: "Гидравлика появляется там, где ручной зажим уже не аргумент. Если деталь может уехать под нагрузкой, значит проблема не в операторе. Проблема в операции, которая оставила усилие неопределённым. Здесь зажим рассчитывается, давление контролируется, точки фиксации работают как система. Мы не продаём железо. Мы проектируем физический запрет на ошибку.",
    cta: "Показать проблемную операцию"
  },
  {
    id: "modular",
    title: "Модульная зажимная оснастка",
    shortTitle: "Модульная",
    headline: ["ДЕТАЛИ МЕНЯЮТСЯ.", "ХАОС ПЕРЕНАЛАДКИ — НЕТ."],
    hook: "Когда номенклатура меняется, переналадка должна быть системой, а не заново собранным цеховым фольклором.",
    pain: "Каждая новая деталь запускает ручную настройку. Оператор ищет упоры, переставляет элементы, проверяет, сомневается. Переналадка ест время и создаёт риск ошибки.",
    controlLoss: "В повторяемости переналадки, позиционировании модулей, фиксации сменных элементов и защите от неправильной сборки оснастки.",
    engineeringSolution: "Создаёт базовую плиту, сменные модули, координатную сетку, штифты, маркировку, упоры и сценарий быстрой переналадки.",
    whenUse: "Когда деталей несколько, операции похожие, но базы и точки зажима отличаются. Для мелко- и среднесерийного производства с регулярной сменой номенклатуры.",
    whenNotUse: "Когда деталь одна и выгоднее специальная оснастка. Когда разброс изделий слишком большой и модульность превращается в компромисс.",
    calculationData: "Семейство деталей, 3D-модели, общие базы, разные зоны зажима, частота переналадки, допустимое время смены, габариты станка, доступ инструмента.",
    questions: ["Сколько разных деталей обрабатывается?","Что у них общее?","Что меняется при переналадке?","Сколько времени занимает смена?","Где чаще ошибаются?","Кто выполняет переналадку?"],
    renderCard: "/media/clamping/modular/mw-pulse-clamping-modular-card-01.png?v=1",
    renderCaption: "Модульная оснастка · render · concept view",
    renderPhoto: "/media/clamping/modular/mw-pulse-clamping-modular-live-shop.jpg?v=1",
    photoCaption: "Модульная оснастка · живое фото на станке",
    stepBackgrounds: {
      hook: "/media/pulse-bg/hook-screen.png",
      pain: "/media/clamping/modular/mw-pulse-clamping-modular-live-shop.jpg?v=1",
      loss: "/media/pulse-bg/bg-04.png",
      fix: "/media/clamping/modular/mw-pulse-clamping-modular-card-01.png?v=1",
      benefit: "/media/clamping/modular/mw-pulse-clamping-modular-live-shop.jpg?v=1",
      cta: "/media/pulse-bg/hook-screen.png",
    },
    callouts: [
      ["МОДУЛЬНЫЕ ПРИЖИМЫ","Быстрая установка и надёжная фиксация"],
      ["БАЗИРУЮЩИЕ ОПОРЫ","Стабильное повторяемое позиционирование"],
      ["УНИВЕРСАЛЬНЫЕ ЭЛЕМЕНТЫ","Под разные формы и размеры деталей"],
      ["УПОРНЫЙ МОДУЛЬ","Точное позиционирование и контроль базы"],
      ["МОДУЛЬНАЯ СЕТКА","Совместимость элементов"],
      ["БАЗОВАЯ ПЛИТА","Жёсткость и стабильность операции"]
    ],
    metrics: [
      ["Модульная сетка","50×50 mm"],
      ["Совместимость","100+ элементов"],
      ["Переналадка","в 3–5 раз быстрее"],
      ["Повторяемость","±0.01 mm"]
    ],
    gallery: [
      {src:"/media/clamping/modular/mw-pulse-clamping-modular-live-shop.jpg?v=1",caption:"Модульная оснастка на станке",value:"Живое фото установки"},
      {src:"/media/clamping/modular/mw-pulse-clamping-modular-card-01.png?v=1",caption:"Модульная оснастка",value:"Одна база — много решений"},
      {src:"/media/clamping/modular/mw-pulse-clamping-modular-card-02.png?v=1",caption:"Модульная оснастка · конфигурация 02",value:"Универсальные элементы на сетке"}
    ],
    // модели нет — второй render вместо model
    renderCardAlt: "/media/clamping/modular/mw-pulse-clamping-modular-card-02.png?v=1",
    renderCaptionAlt: "Модульная оснастка · render 02 · concept view",
    model: null,
    caseRequest: "У нас пять похожих деталей. Под каждую каждый раз собирают установку почти заново.",
    caseImplementation: "Собрали модели семейства деталей, нашли общие базы, разделили постоянные и сменные элементы, сделали координатную плиту и набор модулей под типовые конфигурации.",
    benefit: "Меньше хаоса при переналадке, быстрее смена детали, меньше зависимость от конкретного наладчика, понятнее сценарий установки.",
    speakerNotes: "Модульность — это не «универсальность на все случаи». Это дисциплина переналадки. Когда детали меняются, но база, логика и точки фиксации остаются управляемыми. Без модульной системы каждая новая партия превращается в маленький проект руками оператора. А это не гибкость. Это потеря контроля под видом опыта.",
    cta: "Показать проблемную операцию"
  },
  {
    id: "special",
    title: "Специальная зажимная оснастка",
    shortTitle: "Специальная",
    headline: ["ЕСЛИ ОПЕРАЦИЯ ПОВТОРЯЕТСЯ,", "ХВАТИТ КАЖДЫЙ РАЗ РЕШАТЬ ЕЁ РУКАМИ."],
    hook: "Специальная оснастка нужна там, где операция уже доказала: она повторяется часто и дорого ошибается.",
    pain: "Есть конкретная деталь, конкретная операция и конкретный повторяющийся геморрой: перекос, долгий зажим, нестабильный размер, ручная подгонка, зависимость от одного «золотого» оператора.",
    controlLoss: "В уникальной геометрии детали, недостаточной базе, слабой фиксации, неправильной ориентации, доступе инструмента и повторяемости.",
    engineeringSolution: "Проектирует оснастку под конкретную деталь и операцию: базы, упоры, прижимы, защиту от ошибки, доступ инструмента и порядок установки.",
    whenUse: "Когда операция повторяется регулярно, имеет измеримые потери и стандартные решения не закрывают геометрию или такт.",
    whenNotUse: "Когда операция единичная, данные неполные, деталь ещё меняется или проблема вообще в программе, инструменте либо заготовке.",
    calculationData: "Полная КД, 3D, схема операции, допуски, объём партии, проблемы текущей установки, фото/видео процесса, станок, инструмент, ограничения участка.",
    questions: ["Что именно повторяется?","Где теряется время?","Какой дефект появляется?","Что оператор делает вручную?","Какая партия?","Какой размер критичен?","Что уже пробовали?"],
    renderCard: "/media/clamping/special/mw-pulse-clamping-special-card-01.png?v=1",
    renderCaption: "Специальная оснастка · HYUNDAI KH1000 · render · concept view",
    stepBackgrounds: {
      hook: "/media/pulse-bg/hook-screen.png",
      pain: "/media/clamping/special/mw-pulse-clamping-special-card-01.png?v=1",
      loss: "/media/pulse-bg/bg-05.png",
      fix: "/media/clamping/special/mw-pulse-clamping-special-card-01.png?v=1",
      benefit: "/media/clamping/special/mw-pulse-clamping-special-card-01.png?v=1",
      cta: "/media/pulse-bg/hook-screen.png",
    },
    callouts: [
      ["ГИДРОЦИЛИНДР","ISO 6020/2 · прижим к базовым опорам"],
      ["БАЗОВАЯ ПОВЕРХНОСТЬ","Интерфейс оснастки и плиты станка"],
      ["ГИДРОПРИЖИМ","Фиксация с усилием и повторяемостью"],
      ["ФИКСАЦИЯ ПРИЗМАМИ","Защита от смещения и поворота"],
      ["ОПОРНЫЕ ПРИЗМЫ","Точное положение детали"],
      ["БАЗОВАЯ ПЛИТА","Установка на HYUNDAI KH1000"]
    ],
    metrics: [
      ["Усилие зажима","до 50 kN на цилиндр"],
      ["Давление","до 16 MPa"],
      ["Повторяемость","±0.01 mm"],
      ["Масса оснастки","~820 кг"],
      ["Станок","HYUNDAI KH1000"]
    ],
    gallery: [
      {src:"/media/clamping/special/mw-pulse-clamping-special-card-01.png?v=1",caption:"Специальная оснастка KH1000",value:"Под конкретную деталь и операцию"}
    ],
    model: {
      src: "/models/clamping/special/mw-pulse-clamping-special-model-01.glb?v=1",
      poster: "/media/clamping/special/mw-pulse-clamping-special-model-preview-01.png?v=1",
    },
    caseRequest: "Есть серийная деталь. Каждый раз долго ловим положение, а брак появляется не всегда, но когда появляется — партия уже ушла в переделку.",
    caseImplementation: "Разобрали операцию, нашли место, где деталь допускает неправильную установку, задали индивидуальные базы, добавили контурные опоры и прижимы под конкретную геометрию.",
    benefit: "Установка становится повторяемой, снижается ручная подгонка, меньше риск брака, проще вводить нового оператора.",
    speakerNotes: "Специальная оснастка появляется не потому, что хочется «красивое решение». Она появляется, когда одна и та же операция снова и снова забирает время, нервы и деньги. Если деталь физически можно поставить криво — рано или поздно её поставят криво. Специальная оснастка делает правильное положение единственным рабочим вариантом.",
    cta: "Показать проблемную операцию"
  }
];
"""

HTML_HEAD = r'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>DIR-01 · Metalwork Pulse</title>
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.5.0/model-viewer.min.js"></script>
<style>
/* Tokens from Snapdeck v1 — https://chinmayshringi.github.io/snapdeck/ */
:root{
  --font-sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --font-display: var(--font-sans);
  --ink: #f4f1ea;
  --ink-dim: #8a8680;
  --ink-faint: #4d4a46;
  --canvas: #0a0a0a;
  --canvas-raised: #121212;
  --canvas-sunk: #050505;
  --rule: #242424;
  --rule-strong: #3d3d3d;
  --accent: #b8ff3e;
  --accent-ink: #0a0a0a;
  --nav-h: 56px;
  --glass: rgba(244,241,234,.07);
  --glass-strong: rgba(244,241,234,.12);
  --glass-border: rgba(244,241,234,.12);
  --panel-soft: rgba(10,10,10,.55);
  --panel-hard: rgba(5,5,5,.72);
  --header-bg: rgba(10,10,10,.82);
  --veil: linear-gradient(90deg, rgba(10,10,10,.82) 0%, rgba(10,10,10,.55) 42%, rgba(10,10,10,.78) 100%), linear-gradient(180deg, rgba(10,10,10,.35) 0%, transparent 30%, rgba(10,10,10,.55) 100%);
  --win-hover: rgba(18,18,18,.75);
  --win-active: linear-gradient(145deg,rgba(184,255,62,.1),rgba(18,18,18,.7));
  --beat: 0;
  --beat-scale: 1;
  --glitch-x: 0px;
  --glitch-y: 0px;
  --glitch-skew: 0deg;
  --glitch-rgb: 0;
  --glitch-scan: 0;
}
*{box-sizing:border-box}
html,body{margin:0;height:100%;overflow:hidden;background:var(--canvas);color:var(--ink);font-family:var(--font-sans);-webkit-font-smoothing:antialiased}
button,a.btn{font:inherit;color:inherit;background:none;border:none;cursor:pointer;text-decoration:none}
.mono{font-family:var(--font-mono);letter-spacing:.2em;text-transform:uppercase;font-size:11px;font-weight:400}
.app{height:100dvh;max-height:100dvh;display:flex;flex-direction:column;background:var(--canvas);overflow:hidden}
/* Demo beat pulse + light glitch */
.beat-pulse{display:none}
.beat-glitch{
  position:fixed;inset:0;pointer-events:none;z-index:238;opacity:0;
  background:
    repeating-linear-gradient(
      0deg,
      transparent 0 2px,
      rgba(255,255,255,calc(0.012 * var(--glitch-scan))) 2px 3px
    );
  mix-blend-mode:overlay;
  transition:opacity .05s linear;
}
body.is-demo-beat .beat-glitch{opacity:calc(0.1 + var(--beat) * 0.35)}
body.is-demo-beat.is-glitching .beat-glitch{
  opacity:calc(0.22 + var(--beat) * 0.35);
  box-shadow:
    inset calc(var(--glitch-rgb) * 1.5px) 0 0 rgba(120,180,255,.1),
    inset calc(var(--glitch-rgb) * -1.5px) 0 0 rgba(255,80,120,.08);
}
/* Pulse only on media/bg — never scale .app (clips text via overflow:hidden) */
body.is-demo-beat .left-bg-layer.on{
  transform:scale(calc(1.02 + var(--beat) * 0.03));
  transform-origin:center center;
  filter:contrast(calc(1.04 + var(--beat) * 0.08)) brightness(calc(1 + var(--beat) * 0.12));
  will-change:transform,filter;
}
body.is-demo-beat .slide.has-step-bg .slide-bg{
  transform:scale(calc(1 + var(--beat) * 0.03));
  transform-origin:center center;
  filter:contrast(calc(1.03 + var(--beat) * 0.07)) brightness(calc(1 + var(--beat) * 0.1));
  will-change:transform,filter;
}
body.is-demo-beat .card-media,
body.is-demo-beat .model-preview,
body.is-demo-beat .model-preview-lg{
  overflow:hidden;
}
body.is-demo-beat .card-media img,
body.is-demo-beat .model-preview model-viewer,
body.is-demo-beat .model-preview-lg model-viewer{
  transform:scale(calc(1 + var(--beat) * 0.03));
  transform-origin:center center;
  filter:brightness(calc(1 + var(--beat) * 0.08));
}
body.is-demo-beat .type-win.active{
  border-color:color-mix(in srgb, var(--accent) calc(40% + var(--beat) * 40%), var(--rule-strong));
}
body.is-demo-beat .hero-title,
body.is-demo-beat .parallax-title{
  text-shadow:
    calc(var(--glitch-rgb) * 0.6px) 0 0 rgba(120,180,255,calc(var(--beat) * 0.22)),
    calc(var(--glitch-rgb) * -0.6px) 0 0 rgba(255,90,120,calc(var(--beat) * 0.18));
}
body.is-demo-beat .slide-body,
body.is-demo-beat .slide-body h2,
body.is-demo-beat .glass{
  overflow:visible;
}
body.is-demo-beat .slide:not(.is-media){
  overflow:visible;
}
@media (prefers-reduced-motion:reduce){
  body.is-demo-beat .left-bg-layer.on,
  body.is-demo-beat .slide.has-step-bg .slide-bg,
  body.is-demo-beat .card-media img,
  body.is-demo-beat .model-preview model-viewer,
  body.is-demo-beat .model-preview-lg model-viewer{transform:none;filter:none}
  body.is-demo-beat .beat-glitch{display:none}
  body.is-demo-beat .hero-title,
  body.is-demo-beat .parallax-title{text-shadow:none}
}
.header{height:var(--nav-h);display:flex;align-items:center;justify-content:space-between;gap:16px;padding:0 28px;border-bottom:1px solid var(--rule);background:var(--header-bg);backdrop-filter:blur(12px);position:sticky;top:0;z-index:20}
.brand{display:flex;align-items:center;gap:10px;min-width:0}
.brand-mark{width:14px;height:14px;display:grid;gap:2px}
.brand-mark i{display:block;height:2px;background:var(--accent)}
.brand-name{font-size:14px;font-weight:600;letter-spacing:-.02em;color:var(--ink)}
.brand-name span{color:var(--ink-dim);font-weight:400}
.header-actions{display:flex;align-items:center;gap:10px}
.btn{border:1px solid var(--rule-strong);padding:10px 16px;font-size:13px;font-weight:600;letter-spacing:-.01em;border-radius:0;min-height:40px;transition:background .15s,border-color .15s,color .15s;display:inline-flex;align-items:center;gap:6px}
.btn:hover{border-color:var(--ink-dim)}
.btn-primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn-primary:hover{filter:brightness(1.05);color:var(--accent-ink);border-color:var(--accent)}
.btn-ghost{color:var(--ink-dim)}
.btn:disabled{opacity:.3;cursor:default}
.btn-demo{
  border-color:var(--accent);
  color:var(--accent);
  min-width:96px;
  gap:8px;
}
.btn-demo:hover{background:rgba(184,255,62,.1)}
.btn-demo.is-playing{
  background:var(--accent);
  color:var(--accent-ink);
}
.btn-demo-quiet{
  border-color:var(--rule-strong);
  color:var(--ink-dim);
}
.btn-demo-quiet:hover{border-color:var(--ink-dim);background:rgba(244,241,234,.04);color:var(--ink)}
.btn-demo-quiet.is-playing{
  background:var(--ink);
  color:var(--canvas);
  border-color:var(--ink);
}
.demo-icon{font-size:12px;line-height:1;display:inline-block;width:12px;text-align:center}
/* PDF export deck */
.pdf-root{display:none}
body.pdf-export .app,
body.pdf-export .flashlight,
body.pdf-export .beat-pulse,
body.pdf-export .beat-glitch,
body.pdf-export .cursor-dot,
body.pdf-export .overlay{display:none !important}
html.pdf-export,body.pdf-export{
  overflow:auto !important;
  height:auto !important;
  max-height:none !important;
  background:#0a0a0a !important;
  cursor:auto !important;
}
body.pdf-export,body.pdf-export *{cursor:auto !important}
body.pdf-export .pdf-root{
  display:block !important;
  position:relative;
  z-index:300;
  min-height:100vh;
  background:#0a0a0a;
  color:#f4f1ea;
}
.pdf-toolbar{
  position:sticky;top:0;z-index:50;
  display:flex;gap:10px;align-items:center;justify-content:space-between;flex-wrap:wrap;
  padding:12px 20px;border-bottom:1px solid #242424;background:rgba(10,10,10,.98);
}
.pdf-page{
  position:relative;
  width:100%;
  height:100vh;
  min-height:100vh;
  max-height:100vh;
  padding:0;
  box-sizing:border-box;
  page-break-after:always;
  break-after:page;
  overflow:hidden;
  background:#0a0a0a;
  color:#f4f1ea;
  display:flex;
  align-items:center;
  justify-content:center;
}
.pdf-page:last-child{page-break-after:auto;break-after:auto}
.pdf-page-bg{
  position:absolute;inset:0;
  background-size:cover;background-position:center;
  opacity:.32;filter:saturate(1.05) contrast(1.05);
}
.pdf-page-veil{
  position:absolute;inset:0;
  background:linear-gradient(105deg,rgba(10,10,10,.9),rgba(10,10,10,.58) 50%,rgba(10,10,10,.88));
}
.pdf-page-inner{
  position:relative;z-index:2;
  width:min(1100px,88vw);
  max-height:min(86vh,900px);
  margin:0 auto;
  display:flex;
  flex-direction:column;
  justify-content:center;
  overflow:hidden;
}
.pdf-kicker{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#b8ff3e;margin:0 0 10px}
.pdf-meta{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#8a8680;margin:0 0 14px}
.pdf-title{font-size:clamp(1.8rem,4vw,3.2rem);line-height:.92;letter-spacing:-.04em;font-weight:700;margin:0 0 14px;max-width:16ch}
.pdf-title .acc{color:#b8ff3e}
.pdf-body{
  display:inline-block;max-width:46ch;padding:14px 16px;
  background:rgba(5,5,5,.78);border:1px solid rgba(244,241,234,.12);
  font-size:clamp(1rem,1.3vw,1.15rem);line-height:1.5;color:#f4f1ea;
}
.pdf-media{
  margin-top:12px;border:1px solid rgba(244,241,234,.12);
  background:#050505;padding:10px;text-align:center;
  flex:0 1 auto;min-height:0;
}
.pdf-media img{max-width:100%;max-height:min(52vh,480px);width:auto;object-fit:contain}
.pdf-callouts{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.pdf-callouts span{
  font-family:ui-monospace,Menlo,Consolas,monospace;font-size:10px;letter-spacing:.14em;
  text-transform:uppercase;color:#b8ff3e;border-left:1px solid #b8ff3e;padding-left:8px;
}
.pdf-metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:10px}
.pdf-metrics div{border-top:1px solid #242424;padding-top:8px}
.pdf-metrics b{display:block;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#b8ff3e;font-weight:400}
.pdf-metrics span{font-size:12px;color:#8a8680}
.pdf-speaker{
  margin-top:14px;padding:12px 14px 12px 16px;
  border:1px solid rgba(184,255,62,.22);
  border-left:3px solid #b8ff3e;
  background:linear-gradient(135deg,rgba(184,255,62,.07),rgba(5,5,5,.82) 42%,rgba(5,5,5,.9));
  max-width:72ch;
}
.pdf-speaker-label{
  font-family:ui-monospace,Menlo,Consolas,monospace;
  font-size:10px;letter-spacing:.22em;text-transform:uppercase;
  color:#b8ff3e;margin:0 0 6px;
}
.pdf-speaker-text{margin:0;font-size:clamp(.88rem,1.1vw,1rem);line-height:1.42;color:#c8c4bb}
.pdf-page.has-speaker .pdf-media img{max-height:min(36vh,320px)}
@media print{
  .pdf-toolbar{display:none !important}
  html.pdf-export,body.pdf-export{overflow:visible !important;height:auto !important}
  body.pdf-export{background:#0a0a0a}
  .pdf-page{
    height:100vh;min-height:100vh;max-height:100vh;
    width:100%;padding:0;
    display:flex;align-items:center;justify-content:center;
  }
  .pdf-page-inner{width:90%;max-height:88vh}
  .pdf-media img{max-height:48vh}
  .pdf-page.has-speaker .pdf-media img{max-height:min(34vh,300px)}
  .pdf-speaker{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  @page{size:A4 landscape;margin:0}
}
/* Type windows — top rail, full width, compact */
.type-rail{
  display:grid;
  grid-template-columns:repeat(5,minmax(0,1fr));
  gap:8px;
  padding:8px 16px;
  border-bottom:1px solid var(--rule);
  background:var(--panel-soft);
  backdrop-filter:blur(14px);
  position:relative;z-index:15;
}
.type-win{
  min-width:0;width:100%;
  text-align:left;padding:8px 12px;
  border:1px solid var(--glass-border);
  background:var(--glass);
  backdrop-filter:blur(12px);
  transition:border-color .15s,background .15s,box-shadow .15s;
}
.type-win:hover{border-color:var(--accent);background:var(--win-hover)}
.type-win.active{
  border-color:var(--accent);
  box-shadow:0 0 0 1px color-mix(in srgb, var(--accent) 20%, transparent),0 8px 20px rgba(0,0,0,.15);
  background:var(--win-active);
}
.type-win .ref{font-family:var(--font-mono);font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:4px}
.type-win.active .ref{color:var(--accent)}
.type-win .name{font-size:13px;font-weight:700;letter-spacing:-.03em;line-height:1.1;color:var(--ink-dim)}
.type-win.active .name{color:var(--ink)}
.type-win .hint{margin-top:5px;font-size:11px;line-height:1.3;color:var(--ink-faint);display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.type-win.active .hint{color:var(--ink-dim)}

/* Left back to pre-middle-column width; right takes the rest */
.main{flex:1 1 auto;display:grid;grid-template-columns:minmax(280px,30vw) minmax(0,1fr);min-height:0;align-items:stretch;overflow:hidden}
.col{min-height:0;overflow:hidden;display:flex;flex-direction:column;justify-content:center}
.left{padding:0 32px;border-right:1px solid var(--rule);position:relative;overflow:hidden}
.right{position:relative;padding:0;justify-content:stretch;min-height:0;overflow:hidden}
.right .thought-shell{flex:1 1 auto;min-height:0;overflow:hidden;height:100%}
.left-bg{position:absolute;inset:0;z-index:0;pointer-events:none}
.left-bg-layer{
  position:absolute;inset:0;
  background-size:cover;
  background-position:center 40%;
  background-repeat:no-repeat;
  opacity:0;
  transform:scale(1.06);
  transition:opacity .8s ease, transform 1.2s ease;
  filter:saturate(.9) contrast(1.05);
}
.left-bg-layer.on{opacity:1;transform:scale(1.02)}
.left-veil{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:var(--veil);
}
.stack{width:100%;max-width:420px;margin:0 auto;display:flex;flex-direction:column;justify-content:center;min-height:0;height:100%;position:relative;z-index:2}
.left .stack{max-width:380px;margin:0;padding-left:8px}
.left .hero-title{text-shadow:0 2px 24px rgba(0,0,0,.55)}
.left .hero-kicker{text-shadow:0 1px 12px rgba(0,0,0,.4)}
.hero-kicker{font-family:var(--font-mono);font-size:11px;letter-spacing:.25em;text-transform:uppercase;color:var(--ink-faint);margin:0 0 20px}
.hero-title{font-family:var(--font-display);font-size:clamp(1.6rem,3.4vw,3.2rem);line-height:.9;letter-spacing:-.04em;font-weight:700;margin:0;text-transform:none;max-width:14ch}
.hero-title .dim{color:var(--ink-dim)}
.hero-title .acc{color:var(--accent)}
.heartbeat{width:min(100%,220px);height:24px;margin:28px 0 0}
.heartbeat path{stroke:var(--accent);fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:900;stroke-dashoffset:900;animation:draw 5s ease-in-out infinite}
@keyframes draw{0%{stroke-dashoffset:900}45%{stroke-dashoffset:0}100%{stroke-dashoffset:0}}
@media (prefers-reduced-motion:reduce){.heartbeat path{animation:none;stroke-dashoffset:0}}
.thought-shell{flex:1;display:flex;align-items:stretch;justify-content:stretch;min-height:0;position:relative;width:100%;height:100%}
.slide{width:100%;max-width:560px;margin:0 auto;display:flex;flex-direction:column;justify-content:center;padding:56px 40px 52px;min-height:0;height:100%;position:relative;overflow:hidden}
.slide:not(.is-media){justify-content:center}
.slide.is-media{
  max-width:none;width:100%;height:100%;min-height:0;
  margin:0;padding:36px 16px 48px;
  justify-content:stretch;
  overflow:hidden;
}
.slide.is-media .slide-top{left:16px;right:16px;top:8px}
.slide.is-media .slide-body.wide{
  max-width:none;width:100%;height:100%;
  flex:1 1 auto;min-height:0;
  display:flex;flex-direction:column;
}
.slide.is-media .visual-card-lg,
.slide.is-media .model-card-lg{
  max-width:none;width:100%;
  flex:1 1 auto;min-height:0;
  display:flex;flex-direction:column;
}
.slide.is-media .card-media-lg,
.slide.is-media .model-preview-lg{
  flex:1 1 auto;min-height:0;
  height:auto !important;
  overflow:hidden;
}
.slide.is-media .card-media-lg img{
  max-height:100%;max-width:100%;width:auto;height:auto;
  object-fit:contain;
}
.slide.is-media .model-preview-lg model-viewer{
  min-height:0 !important;height:100% !important;
}
.slide.is-media .callouts,
.slide.is-media .metrics-bar,
.slide.is-media .card-actions,
.slide.is-media .model-controls,
.slide.is-media .card-label{flex:0 0 auto}
.slide.is-media .callouts{padding:8px 12px;gap:6px}
.slide.is-media .metrics-bar{padding:8px 12px;gap:6px}
.slide.is-media .card-label{padding:8px 12px}
.slide.is-media .callouts b{font-size:9px}
.slide.is-media .metric b{font-size:9px}
.slide.is-media .metric span{font-size:11px}
/* Nav always at bottom of right panel: prev left, next right */
.slide-foot{
  position:absolute;bottom:10px;left:12px;right:12px;
  display:flex;align-items:center;justify-content:space-between;gap:8px;z-index:8;
}
.slide.is-media .slide-foot{left:12px;right:12px;bottom:8px}
.slide-foot .btn{min-height:34px;padding:8px 12px}
@media (max-height:820px){
  .slide.is-media .metrics-bar{display:none}
}
@media (max-height:700px){
  .slide.is-media .callouts{display:none}
  .slide.is-media{padding:32px 12px 44px}
}
.slide.has-step-bg{max-width:100%;min-height:100%;padding:56px 48px 52px}
.slide-bg{
  position:absolute;inset:0;z-index:0;pointer-events:none;
  background-size:cover;background-position:center;background-repeat:no-repeat;
  opacity:0;transition:opacity .55s ease;
  filter:saturate(1.02) contrast(1.04);
}
.slide.has-step-bg .slide-bg{opacity:1}
.slide-bg-veil{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:var(--veil);
  opacity:0;transition:opacity .55s ease;
}
.slide.has-step-bg .slide-bg-veil{opacity:1}
.slide.has-step-bg .slide-body,
.slide.has-step-bg .slide-top,
.slide.has-step-bg .slide-foot{z-index:2}
.slide.has-step-bg .slide-body h2{text-shadow:0 2px 28px rgba(0,0,0,.45)}
.slide.has-step-bg .glass{
  background:var(--panel-hard);
  border-color:var(--glass-border);
}
.thought-shell:has(.has-step-bg){align-items:stretch}
.slide-top{position:absolute;top:24px;left:48px;right:48px;display:flex;align-items:baseline;justify-content:space-between;gap:16px}
.slide-top .section-id{font-family:var(--font-mono);font-size:11px;letter-spacing:.25em;text-transform:uppercase;color:var(--ink-faint)}
.slide-top .section-id b{color:var(--accent);font-weight:400}
.app.is-fs .header{display:none}
.app.is-fs .main{grid-template-columns:1fr}
.app.is-fs .left{display:none}
.app.is-fs .slide{max-width:720px;min-height:80vh}
.app.is-fs .slide.is-media{max-width:none;min-height:0;height:100%}
.app.is-fs .type-rail{padding:14px 24px}
.slide-body{display:flex;flex-direction:column;justify-content:center;align-items:flex-start;width:100%;max-width:min(520px,100%);position:relative;z-index:2}
.slide-body.wide{max-width:min(100%,100%)}
.slide-body .type-name{font-family:var(--font-mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-faint);margin:0 0 16px}
.slide-body h2{margin:0;font-family:var(--font-display);font-size:clamp(2rem,4.2vw,3.75rem);line-height:.9;letter-spacing:-.04em;font-weight:700;max-width:14ch}
.slide-body h2 .acc{color:var(--accent)}
.slide-body h2 .dim{color:var(--ink-dim)}
/* Liquid glass description plate */
.glass{
  margin:28px 0 0;
  padding:18px 22px;
  max-width:min(46ch,100%);
  width:100%;
  font-size:clamp(1.05rem,1.25vw,1.2rem);
  line-height:1.55;
  letter-spacing:-.01em;
  font-weight:400;
  color:var(--ink);
  background:var(--glass-strong);
  border:1px solid var(--glass-border);
  backdrop-filter:blur(18px) saturate(1.2);
  -webkit-backdrop-filter:blur(18px) saturate(1.2);
  box-shadow:0 1px 0 color-mix(in srgb, var(--ink) 8%, transparent) inset,0 16px 40px rgba(0,0,0,.12);
  border-radius:2px;
  position:relative;
  overflow:hidden;
}
.glass::before{
  content:"";
  position:absolute;inset:0;
  background:linear-gradient(120deg,transparent 30%,color-mix(in srgb, var(--accent) 10%, transparent) 48%,transparent 62%);
  pointer-events:none;
  opacity:.7;
}
.glass > span{position:relative;z-index:1;display:block}
.edge-dots{position:absolute;right:16px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:10px;z-index:5}
/* Parallax layers */
.parallax-title{will-change:transform;transition:transform .12s ease-out}
.parallax-glass{will-change:transform;transition:transform .18s ease-out}
.parallax-meta{will-change:transform;transition:transform .22s ease-out}
/* Custom cursor + flashlight */
@media (pointer:fine){
  body,body *{cursor:none !important}
}
.cursor-dot{
  position:fixed;top:0;left:0;pointer-events:none;z-index:200;border-radius:50%;
  width:5px;height:5px;background:var(--accent);
  transform:translate(-50%,-50%);
  box-shadow:0 0 14px rgba(184,255,62,.85);
}
.flashlight{
  position:fixed;inset:0;pointer-events:none;z-index:1;
  background:radial-gradient(
    420px circle at var(--mx,50%) var(--my,50%),
    rgba(184,255,62,.09) 0%,
    rgba(184,255,62,.03) 22%,
    transparent 48%
  );
  opacity:.9;
  transition:opacity .3s;
}
@media (prefers-reduced-motion:reduce){
  .parallax-title,.parallax-glass,.parallax-meta{transition:none;transform:none !important}
  .flashlight{display:none}
  body,body *{cursor:auto !important}
  .cursor-dot{display:none}
}
.edge-dots .dot{width:8px;height:8px;border-radius:50%;background:var(--rule-strong);padding:0;min-height:0;border:0}
.edge-dots .dot.on{background:var(--accent)}
.visual-card,.model-card{
  position:relative;border:1px solid var(--glass-border);background:var(--panel-hard);
  overflow:hidden;max-width:640px;width:100%;
  backdrop-filter:blur(14px) saturate(1.15);
  -webkit-backdrop-filter:blur(14px) saturate(1.15);
  box-shadow:0 1px 0 color-mix(in srgb, var(--ink) 6%, transparent) inset,0 18px 40px rgba(0,0,0,.18);
}
.visual-card-lg,.model-card-lg{max-width:100%}
.visual-card{cursor:zoom-in}
.model-card-lg{cursor:grab}
.model-card-lg:active{cursor:grabbing}
.model-card-lg model-viewer{cursor:grab}
.model-card-lg model-viewer:active{cursor:grabbing}
.render-screen,.model-screen{max-width:100%;width:100%;height:100%;min-height:0}
.render-head{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:12px;width:100%}
.render-title{font-size:clamp(1.5rem,2.6vw,2.25rem) !important;max-width:16ch !important;text-transform:uppercase}
.card-label{padding:10px 14px;border-bottom:1px solid var(--rule)}
.card-label .l1{font-family:var(--font-mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent)}
.card-label .l2{font-family:var(--font-mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-faint);margin-top:4px}
.card-media{min-height:240px;display:flex;align-items:center;justify-content:center;padding:20px;background:var(--canvas-sunk)}
.card-media-lg{min-height:0;padding:10px;display:flex;align-items:center;justify-content:center}
.card-media img{max-width:100%;max-height:300px;object-fit:contain;display:block}
.card-media-lg img{max-height:100%;width:auto;max-width:100%;object-fit:contain}
.card-media-photo{background:#0a0a0a}
.card-media-photo img{object-fit:contain;width:100%;height:100%}
/* Live photo: centered with balanced breathing room */
.slide.is-media:has(#photoCard){
  padding:48px 40px 56px;
}
.slide.is-media:has(#photoCard) .slide-body.wide{
  justify-content:center;
  align-items:center;
  height:100%;
}
.slide.is-media:has(#photoCard) .visual-card-lg{
  width:min(68%,720px);
  max-width:720px;
  height:auto;
  max-height:min(58%,520px);
  margin:auto;
  flex:0 1 auto;
  display:flex;
  flex-direction:column;
}
.slide.is-media:has(#photoCard) .card-label{
  padding:10px 14px;
}
.slide.is-media:has(#photoCard) .card-media-lg{
  flex:0 1 auto;
  padding:18px 22px 22px;
  max-height:none;
}
.slide.is-media:has(#photoCard) .card-media-lg img{
  display:block;
  width:100%;
  height:auto;
  max-height:min(42vh,360px);
  max-width:100%;
  object-fit:contain;
  margin:0 auto;
}
.callouts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px}
.callouts span{display:block;font-size:11px;color:var(--ink-faint);margin-top:3px;letter-spacing:0;text-transform:none;font-family:var(--font-sans)}
.metrics-bar{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px;
  padding:12px 16px;border-top:1px solid var(--rule);
}
.metric b{display:block;font-family:var(--font-mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:400;margin-bottom:4px}
.metric span{font-size:12px;color:var(--ink-dim);line-height:1.3}
.card-hint{font-family:var(--font-mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-faint);margin-left:auto}
.thumb{width:72px;height:52px;padding:0;border:1px solid var(--rule);overflow:hidden;background:var(--canvas-sunk)}
.thumb img,.thumb .placeholder{width:100%;height:100%;object-fit:cover;min-height:0}
.thumb .placeholder{padding:4px;font-size:8px}
.model-preview-lg{height:min(50vh,420px) !important;min-height:320px}
.model-preview-lg model-viewer{display:block}
.placeholder{width:100%;min-height:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:20px;text-align:center;color:var(--ink-faint)}
.placeholder .ph-title{font-family:var(--font-mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent)}
.placeholder .ph-file{font-family:var(--font-mono);font-size:11px;color:var(--ink-faint);word-break:break-all}
.callouts{display:flex;flex-wrap:wrap;gap:10px;padding:14px 16px;border-top:1px solid var(--rule)}
.callouts div{border-left:1px solid var(--accent);padding-left:10px}
.callouts b{display:block;font-family:var(--font-mono);font-size:11px;letter-spacing:.16em;color:var(--accent);font-weight:400}
.card-actions,.model-controls{display:flex;gap:8px;padding:12px 16px;border-top:1px solid var(--rule);flex-wrap:wrap}
.model-card model-viewer,.model-card .model-preview{width:100%;height:300px;background:var(--canvas-sunk)}
.cta-thought{margin-top:24px;display:flex;gap:10px;flex-wrap:wrap}
.slide.is-cta{max-width:min(920px,100%);justify-content:flex-start;padding-top:40px}
.slide.is-cta .slide-body{max-width:100%;justify-content:flex-start;flex:1;min-height:0}
.slide.is-cta .parallax-title{font-size:clamp(1.6rem,3.2vw,2.6rem);max-width:18ch}
.find-us-inline{
  margin-top:14px;flex:1;min-height:0;display:flex;flex-direction:column;
  border:1px solid var(--rule);background:#0a0a0a;width:100%;
}
.find-us-inline-head{
  display:flex;align-items:center;justify-content:space-between;gap:10px;
  padding:8px 12px;border-bottom:1px solid var(--rule);flex-shrink:0;
  background:#0a0a0a;
}
.find-us-inline-head .mono{font-size:10px;color:var(--accent)}
.find-us-body{padding:0 !important;align-items:stretch !important;justify-content:stretch !important;background:#0a0a0a}
.find-us-stage{
  flex:1;min-height:min(48vh,420px);width:100%;height:100%;
  display:flex;align-items:center;justify-content:center;
  background:#0a0a0a;overflow:auto;position:relative;
}
.find-us-stage-inner{position:relative;max-width:100%;max-height:100%;line-height:0}
.find-us-stage canvas{display:block;max-width:100%;max-height:min(78vh,900px);width:auto;height:auto;background:#0a0a0a}
.find-us-inline .find-us-stage canvas{max-height:min(48vh,420px)}
.find-us-links{position:absolute;inset:0}
.find-us-links a{
  position:absolute;display:block;border-radius:2px;cursor:pointer;
}
.find-us-links a:hover{outline:1px solid rgba(184,255,62,.55);outline-offset:2px;background:rgba(184,255,62,.06)}
.find-us-qr-bar{
  display:flex;flex-wrap:wrap;gap:8px;justify-content:center;
  padding:10px 12px 12px;background:#0a0a0a;border-top:1px solid var(--rule);
}
.find-us-qr-bar a{
  font-family:var(--font-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);border:1px solid rgba(184,255,62,.28);padding:8px 10px;text-decoration:none;
}
.find-us-qr-bar a:hover{background:rgba(184,255,62,.1);border-color:var(--accent)}
.find-us-stage.is-loading::after{
  content:"Загрузка…";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  font-family:var(--font-mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-faint);
}
.overlay{position:fixed;inset:0;z-index:100;background:rgba(10,10,10,.96);display:none;flex-direction:column}
.overlay.open{display:flex}
.overlay-head,.overlay-foot{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 24px;border-color:var(--rule);border-style:solid}
.overlay-head{border-bottom-width:1px}.overlay-foot{border-top-width:1px}
.overlay-body{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;padding:16px}
.overlay-body img{max-width:100%;max-height:calc(100dvh - 9rem);object-fit:contain}
.overlay-body model-viewer{width:min(1100px,100%);height:calc(100dvh - 10rem);background:var(--canvas-sunk)}
.overlay-meta{max-width:420px;color:var(--ink-dim);font-size:14px;line-height:1.45}
@media (max-width:980px){
  .header{padding:0 14px;height:52px}
  .brand-name span{display:none}
  .header-actions .btn-primary{padding:10px 12px;font-size:12px}
  .type-rail{
    display:flex;gap:8px;padding:8px 12px;
    overflow-x:auto;-webkit-overflow-scrolling:touch;
    scrollbar-width:thin;
  }
  .type-win{flex:1 0 auto;min-width:120px;max-width:148px;padding:8px 10px}
  .type-win .hint{display:none}
  html,body{overflow:auto}
  .app{height:auto;min-height:100dvh;max-height:none;overflow:visible}
  .main{grid-template-columns:1fr;overflow:visible;min-height:auto}
  .col{overflow:visible;min-height:auto}
  .left{border-right:none;border-bottom:1px solid var(--rule);min-height:38vh;padding:24px 16px}
  .right{min-height:55dvh;padding:0 12px 16px;overflow:hidden}
  .right .thought-shell{min-height:55dvh}
  .stack,.slide{min-height:0;max-width:100%;margin:0;height:100%}
  .stack{padding:8px 0 12px}
  .slide{padding:48px 0 52px}
  .slide-top{left:0;right:0;top:8px}
  .slide-foot{left:8px;right:8px;bottom:8px}
  .slide.is-media{padding:32px 8px 44px;overflow:hidden;height:100%}
  .edge-dots{right:0}
  .hero-title,.slide-body h2{font-size:clamp(1.75rem,7.5vw,2.5rem);max-width:100%}
  .glass{max-width:100%;font-size:1rem}
  .app.is-fs .left{display:none}
  .app.is-fs .type-rail{display:flex}
  .app.is-fs .right{min-height:100dvh}
  /* mobile: no custom cursor */
  body,body *{cursor:auto !important}
  .cursor-dot{display:none}
  .flashlight{opacity:.45}
}
</style>
</head>
<body>
<div class="flashlight" aria-hidden="true"></div>
<div class="beat-pulse" id="beatPulse" aria-hidden="true"></div>
<div class="beat-glitch" id="beatGlitch" aria-hidden="true"></div>
<div class="cursor-dot" id="cursorDot" aria-hidden="true"></div>
<div class="app" id="app">
<header class="header">
  <div class="brand">
    <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span>
    <div class="brand-name">Metalwork Pulse <span>· DIR-01</span></div>
  </div>
  <div class="header-actions">
    <button class="btn btn-demo" id="demoToggle" type="button" aria-label="Demo with music">
      <span class="demo-icon" id="demoIcon">▶</span>
      <span id="demoLabel">Demo</span>
    </button>
    <button class="btn btn-demo btn-demo-quiet" id="demoQuietToggle" type="button" aria-label="Demo without music">
      <span class="demo-icon" id="demoQuietIcon">▶</span>
      <span id="demoQuietLabel">Auto</span>
    </button>
    <button class="btn btn-ghost" id="findUsBtn" type="button">Как нас найти</button>
    <button class="btn btn-ghost" id="pdfExport" type="button">PDF</button>
    <button class="btn btn-ghost" id="pptxExport" type="button">PPTX</button>
    <button class="btn btn-ghost" id="fsToggle" type="button">Fullscreen</button>
    <a class="btn btn-primary" href="mailto:n.zaikovski@icloud.com?subject=Проблемная%20операция%20—%20DIR-01">Показать операцию →</a>
  </div>
</header>
<audio id="demoAudio" src="/media/audio/metalwork-pulse.mp3" preload="auto" loop></audio>
<script src="https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<nav class="type-rail" id="typeList" aria-label="Типы оснастки"></nav>
<main class="main">
<aside class="col left">
  <div class="left-bg" id="leftBg" aria-hidden="true">
    <div class="left-bg-layer on" data-bg="mechanical" style="background-image:url('/media/pulse-bg/bg-01.png')"></div>
    <div class="left-bg-layer" data-bg="pneumatic" style="background-image:url('/media/pulse-bg/bg-02.png')"></div>
    <div class="left-bg-layer" data-bg="hydraulic" style="background-image:url('/media/pulse-bg/bg-03.png')"></div>
    <div class="left-bg-layer" data-bg="modular" style="background-image:url('/media/pulse-bg/bg-04.png')"></div>
    <div class="left-bg-layer" data-bg="special" style="background-image:url('/media/pulse-bg/bg-05.png')"></div>
  </div>
  <div class="left-veil" aria-hidden="true"></div>
  <div class="stack">
    <p class="hero-kicker">01 / clamping</p>
    <h1 class="hero-title">Станок за миллионы<br><span class="dim">бессилен,</span><br><span class="acc">если база — на ощущениях.</span></h1>
    <svg class="heartbeat" viewBox="0 0 1100 300" aria-hidden="true"><path d="M0 150 H175 L210 150 L240 58 L285 230 L330 58 L365 150 H550 L590 150 L625 220 L660 150 L695 220 L730 150 H820 L850 150 L880 36 L912 264 L946 150 H1100"/></svg>
  </div>
</aside>
<section class="col right" id="dossier">
  <div class="thought-shell" id="dossierBody"></div>
</section>
</main>
</div>
<div class="pdf-root" id="pdfRoot" aria-hidden="true"></div>

<div class="overlay" id="renderOverlay" role="dialog" aria-modal="true">
  <div class="overlay-head"><div><div class="mono" style="font-size:10px;color:var(--accent)">RENDER · CONCEPT VIEW</div><div id="renderOverlayTitle" style="font-size:14px;color:var(--muted)"></div></div>
  <button class="btn mono" type="button" data-close="renderOverlay">ESC · Закрыть</button></div>
  <div class="overlay-body" id="renderOverlayBody"></div>
  <div class="overlay-foot mono" style="font-size:9px;color:var(--dim);justify-content:center">MW PULSE · ENGINEERING DIAGNOSTIC CANVAS</div>
</div>

<div class="overlay" id="galleryOverlay" role="dialog" aria-modal="true">
  <div class="overlay-head"><div><div class="mono" style="font-size:10px;color:var(--accent)">Gallery</div><div id="galleryOverlayTitle" style="font-size:14px;color:var(--muted)"></div></div>
  <div style="display:flex;gap:8px"><button class="btn mono" type="button" id="galleryPrev">← Prev</button><button class="btn mono" type="button" id="galleryNext">Next →</button><button class="btn mono" type="button" data-close="galleryOverlay">ESC · Закрыть</button></div></div>
  <div class="overlay-body" style="flex-direction:column;gap:14px"><div id="galleryOverlayMedia" style="flex:1;display:flex;align-items:center;justify-content:center;width:100%"></div><div class="overlay-meta" id="galleryOverlayMeta"></div></div>
  <div class="overlay-foot mono" style="font-size:9px;color:var(--dim);justify-content:center">MW PULSE · ENGINEERING DIAGNOSTIC CANVAS</div>
</div>

<div class="overlay" id="modelOverlay" role="dialog" aria-modal="true">
  <div class="overlay-head"><div><div class="mono" style="font-size:10px;color:var(--accent)">GLB · 3D MODEL</div><div id="modelOverlayTitle" style="font-size:14px;color:var(--muted)"></div></div>
  <button class="btn mono" type="button" data-close="modelOverlay">ESC · Закрыть</button></div>
  <div class="overlay-body" style="flex-direction:column;gap:12px"><div id="modelOverlayMedia" style="flex:1;width:100%;display:flex;align-items:center;justify-content:center"></div><div class="model-controls" id="modelOverlayControls"></div></div>
  <div class="overlay-foot mono" style="font-size:9px;color:var(--dim);justify-content:center">drag to rotate · scroll to zoom</div>
</div>

<div class="overlay" id="findUsOverlay" role="dialog" aria-modal="true" aria-label="Как нас найти">
  <div class="overlay-head">
    <div>
      <div class="mono" style="font-size:10px;color:var(--accent)">CONTACT · QR</div>
      <div style="font-size:14px;color:var(--ink-dim)">Как нас найти</div>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <a class="btn btn-primary" id="findUsOpenPdf" href="/media/contact/find-us.pdf" target="_blank" rel="noopener">Открыть PDF →</a>
      <button class="btn mono" type="button" data-close="findUsOverlay">ESC · Закрыть</button>
    </div>
  </div>
  <div class="overlay-body find-us-body" style="flex-direction:column">
    <div class="find-us-stage is-loading" id="findUsStage" aria-label="Как нас найти">
      <div class="find-us-stage-inner">
        <canvas id="findUsCanvas"></canvas>
        <div class="find-us-links" id="findUsLinks"></div>
      </div>
    </div>
    <div class="find-us-qr-bar" id="findUsQrBar"></div>
  </div>
  <div class="overlay-foot mono" style="font-size:9px;color:var(--ink-faint);justify-content:center">QR кликабельны · PDF без изменений</div>
</div>

<script>
'''

HTML_TAIL = r'''
const VIEWS = {ISO:"45deg 55deg 2.4m",FRONT:"0deg 90deg 2.4m",TOP:"0deg 10deg 2.8m",SIDE:"90deg 90deg 2.4m",RESET:"45deg 55deg 2.4m"};
let activeId = "mechanical";
let stepIndex = 0;
let galleryIndex = 0;

const getType = (id = activeId) => TYPES.find(t => t.id === id);

function stepsFor(t) {
  const steps = [
    { key: "hook", slug: "hook", kind: "text", title: t.headline, body: t.hook },
    { key: "render", slug: "render", kind: "render" },
  ];
  if (t.renderPhoto) {
    steps.push({ key: "photo", slug: "photo", kind: "photo" });
  }
  if (t.model && t.model.src) {
    steps.push({ key: "model", slug: "model", kind: "model" });
  } else if (t.renderCardAlt) {
    steps.push({ key: "renderAlt", slug: "render-2", kind: "renderAlt" });
  }
  steps.push(
    { key: "pain", slug: "pain", kind: "text", title: ["Боль.", "Операции."], body: t.pain },
    { key: "loss", slug: "loss", kind: "text", title: ["Где теряется", "управление."], body: t.controlLoss },
    { key: "fix", slug: "fix", kind: "text", title: ["Инженерное", "решение."], body: t.engineeringSolution },
    { key: "benefit", slug: "gain", kind: "text", title: ["Что", "меняется."], body: t.benefit },
    { key: "cta", slug: "end", kind: "cta" }
  );
  return steps;
}

/** Подложка текстового шага: явная карта типа или авто из медиа блока */
function resolveStepBackground(t, stepKey) {
  if (t.stepBackgrounds && t.stepBackgrounds[stepKey]) {
    return t.stepBackgrounds[stepKey];
  }
  // авто для остальных типов, когда появятся свои фото/рендеры
  const live = t.renderPhoto || null;
  const render = t.renderCard || null;
  const poster = (t.model && t.model.poster) || t.renderCardAlt || render;
  const fallback = {
    hook: "/media/pulse-bg/hook-screen.png",
    pain: live || render,
    loss: render || live,
    fix: poster || render || live,
    benefit: live || render, // slug "gain", key "benefit"
    cta: render || live || "/media/pulse-bg/hook-screen.png",
  };
  return fallback[stepKey] || null;
}

function speakerForStep(t, s) {
  if (s.key === "hook") return t.hook || t.speakerNotes || "";
  if (s.key === "pain") return t.pain || t.speakerNotes || "";
  if (s.key === "loss") return t.controlLoss || t.speakerNotes || "";
  if (s.key === "fix") return t.engineeringSolution || t.speakerNotes || "";
  if (s.key === "benefit") return t.benefit || t.speakerNotes || "";
  if (s.kind === "photo") return t.caseImplementation || t.speakerNotes || "";
  if (s.kind === "render" || s.kind === "renderAlt" || s.kind === "model") return t.speakerNotes || "";
  if (s.kind === "cta") {
    return "Покажите проблемную операцию. Разберём, где теряется управление — и какой оснасткой вернуть ритм. Пишите: n.zaikovski@icloud.com";
  }
  return t.speakerNotes || "";
}

function mediaOrPlaceholder(src, alt) {
  return `<div class="media-wrap" data-src="${src}" data-alt="${String(alt).replace(/"/g, "&quot;")}"></div>`;
}

function hydrateMedia(root = document) {
  root.querySelectorAll(".media-wrap").forEach(wrap => {
    const src = wrap.dataset.src;
    const alt = wrap.dataset.alt || "";
    const img = new Image();
    img.alt = alt;
    img.onload = () => wrap.replaceWith(img);
    img.onerror = () => {
      const file = src.split("/").pop();
      wrap.outerHTML = `<div class="placeholder corners"><i></i><div class="mono ph-title">Asset placeholder</div><div class="mono ph-file">${file}</div></div>`;
    };
    img.src = src;
  });
}

function modelViewerHTML(type, fullscreen = false) {
  const isMobile = window.matchMedia("(max-width: 980px)").matches;
  let src = type.model.src;
  if (isMobile && type.model.mobileSrc) src = type.model.mobileSrc;
  const poster = type.model.poster || "";
  const id = fullscreen ? "fsModelViewer" : "inlineModelViewer";
  const h = fullscreen ? "calc(100dvh - 10rem)" : "100%";
  return `<model-viewer id="${id}" src="${src}" ${poster ? `poster="${poster}"` : ""}
    camera-controls
    touch-action="none"
    shadow-intensity="0.85"
    exposure="1.05"
    field-of-view="32deg"
    min-camera-orbit="auto auto 25%"
    max-camera-orbit="auto auto 200%"
    camera-orbit="${VIEWS.ISO}"
    interaction-prompt="auto"
    interaction-prompt-threshold="0"
    style="width:100%;height:${h};min-height:${fullscreen ? "60vh" : "320px"};background:var(--canvas-sunk);--poster-color:transparent"
    alt="${type.title}"></model-viewer>`;
}

function renderTypeNav() {
  const list = document.getElementById("typeList");
  list.innerHTML = TYPES.map((t, i) => `
    <button class="type-win ${t.id === activeId ? "active" : ""}" type="button" data-type="${t.id}">
      <div class="ref">0${i + 1}</div>
      <div class="name">${t.shortTitle}</div>
      <div class="hint">${t.hook}</div>
    </button>`).join("");
  list.querySelectorAll("[data-type]").forEach(btn => btn.addEventListener("click", () => {
    stopDemo();
    selectType(btn.dataset.type);
  }));
}

function titleHtml(lines) {
  return lines.map((line, i) => {
    const cls = i === lines.length - 1 ? "acc" : (i === 0 ? "" : "dim");
    return i === 0 ? (cls ? `<span class="${cls}">${line}</span>` : line) : `<br><span class="${cls || "dim"}">${line}</span>`;
  }).join("");
}

function renderThought() {
  const t = getType();
  const steps = stepsFor(t);
  if (stepIndex < 0) stepIndex = 0;
  if (stepIndex >= steps.length) stepIndex = steps.length - 1;
  const s = steps[stepIndex];
  const body = document.getElementById("dossierBody");
  const n = String(stepIndex + 1).padStart(2, "0");
  const total = String(steps.length).padStart(2, "0");

  let main = "";
  if (s.kind === "text") {
    main = `<div class="slide-body">
      <p class="type-name parallax-meta">${t.shortTitle}</p>
      <h2 class="parallax-title">${titleHtml(s.title)}</h2>
      ${s.body ? `<div class="glass parallax-glass"><span>${s.body}</span></div>` : ""}
    </div>`;
  } else if (s.kind === "render") {
    const metrics = (t.metrics || []).slice(0,4).map(([a,b]) => `<div class="metric"><b>${a}</b><span>${b}</span></div>`).join("");
    const callouts = (t.callouts || []).slice(0,6).map(([a]) => `<div><b>${a}</b></div>`).join("");
    main = `<div class="slide-body wide render-screen">
      <div class="visual-card visual-card-lg parallax-glass" id="renderCard">
        <div class="card-label">
          <div class="l1">Render · concept</div>
          <div class="l2">${t.shortTitle} · клик на весь экран</div>
        </div>
        <div class="card-media card-media-lg">${mediaOrPlaceholder(t.renderCard, t.title)}</div>
        <div class="callouts callouts-grid">${callouts}</div>
        <div class="metrics-bar">${metrics}</div>
      </div>
    </div>`;
  } else if (s.kind === "photo") {
    main = `<div class="slide-body wide render-screen">
      <div class="visual-card visual-card-lg parallax-glass" id="photoCard">
        <div class="card-label">
          <div class="l1">Photo · shop floor</div>
          <div class="l2">${t.shortTitle} · живое фото · клик на весь экран</div>
        </div>
        <div class="card-media card-media-lg card-media-photo">${mediaOrPlaceholder(t.renderPhoto, t.photoCaption || t.title)}</div>
      </div>
    </div>`;
  } else if (s.kind === "renderAlt") {
    const metrics = (t.metrics || []).slice(0,4).map(([a,b]) => `<div class="metric"><b>${a}</b><span>${b}</span></div>`).join("");
    const callouts = (t.callouts || []).slice(0,6).map(([a]) => `<div><b>${a}</b></div>`).join("");
    main = `<div class="slide-body wide render-screen">
      <div class="visual-card visual-card-lg parallax-glass" id="renderAltCard">
        <div class="card-label">
          <div class="l1">Render · concept 02</div>
          <div class="l2">${t.shortTitle} · вместо 3D · клик на весь экран</div>
        </div>
        <div class="card-media card-media-lg">${mediaOrPlaceholder(t.renderCardAlt, t.title)}</div>
        <div class="callouts callouts-grid">${callouts}</div>
        <div class="metrics-bar">${metrics}</div>
      </div>
    </div>`;
  } else if (s.kind === "model") {
    main = `<div class="slide-body wide model-screen">
      <div class="render-head parallax-meta">
        <div>
          <p class="type-name">glb · 3d model</p>
          <h2 class="parallax-title render-title">Модель<br><span class="acc">оснастки.</span></h2>
        </div>
        <button class="btn btn-primary" type="button" id="openModelBtn">Fullscreen →</button>
      </div>
      <div class="model-card model-card-lg parallax-glass" id="modelCard">
        <div class="model-preview model-preview-lg">${modelViewerHTML(t,false)}</div>
        <div class="model-controls" id="inlineModelControls">
          ${Object.keys(VIEWS).map(v => `<button class="btn" type="button" data-view="${v}">${v}</button>`).join("")}
          <span class="card-hint">Тяни мышью · крути модель</span>
        </div>
      </div>
    </div>`;
  } else if (s.kind === "cta") {
    main = `<div class="slide-body" style="display:flex;flex-direction:column;min-height:0;flex:1">
      <p class="type-name parallax-meta">end</p>
      <h2 class="parallax-title">Покажите<br><span class="acc">проблемную операцию.</span></h2>
      <div class="glass parallax-glass"><span>Разберём, где теряется управление — и какой оснасткой вернуть ритм.</span></div>
      <div class="cta-thought parallax-meta">
        <a class="btn btn-primary" href="mailto:n.zaikovski@icloud.com?subject=Проблемная%20операция%20—%20DIR-01">Показать операцию →</a>
        <button class="btn" type="button" id="findUsCtaBtn">Как нас найти</button>
      </div>
      <div class="find-us-inline parallax-meta">
        <div class="find-us-inline-head">
          <span class="mono">CONTACT · QR</span>
          <a class="btn btn-ghost" href="/media/contact/find-us.pdf" target="_blank" rel="noopener" style="min-height:32px;padding:6px 10px;font-size:12px">Открыть PDF →</a>
        </div>
        <div class="find-us-stage is-loading" id="findUsInlineStage" aria-label="Как нас найти">
          <div class="find-us-stage-inner">
            <canvas></canvas>
            <div class="find-us-links"></div>
          </div>
        </div>
        <div class="find-us-qr-bar" data-find-us-bar></div>
      </div>
    </div>`;
  }

  const isMedia = s.kind === "render" || s.kind === "renderAlt" || s.kind === "photo" || s.kind === "model";
  const isCta = s.kind === "cta";
  const stepBg = !isMedia ? resolveStepBackground(t, s.key) : null;
  const bgStyle = stepBg ? ` style="background-image:url('${stepBg}')"` : "";
  body.innerHTML = `
    <div class="slide ${stepBg ? "has-step-bg" : ""} ${isMedia ? "is-media" : ""} ${isCta ? "is-cta" : ""}">
      <div class="slide-bg parallax-glass" aria-hidden="true"${bgStyle}></div>
      <div class="slide-bg-veil" aria-hidden="true"></div>
      <div class="slide-top parallax-meta">
        <div class="section-id"><b>${n}</b> / ${s.slug}</div>
        <div class="section-id">${n}/${total}</div>
      </div>
      ${main}
      <div class="slide-foot">
        <button class="btn" type="button" id="prevStep" ${stepIndex === 0 ? "disabled" : ""}>←</button>
        <button class="btn btn-primary" type="button" id="nextStep">${stepIndex === steps.length - 1 ? "Again →" : "Next →"}</button>
      </div>
    </div>
    <div class="edge-dots">${steps.map((_, i) => `<button class="dot ${i === stepIndex ? "on" : ""}" type="button" data-step="${i}" aria-label="Step ${i+1}"></button>`).join("")}</div>
  `;

  hydrateMedia(body);
  body.querySelectorAll("[data-step]").forEach(btn => btn.addEventListener("click", () => { stepIndex = Number(btn.dataset.step); renderThought(); }));
  document.getElementById("prevStep").addEventListener("click", () => {
    if (demoPlaying && !demoAdvancing) stopDemo();
    if (stepIndex > 0) { stepIndex--; renderThought(); }
  });
  document.getElementById("nextStep").addEventListener("click", () => {
    if (demoPlaying && !demoAdvancing) stopDemo();
    if (stepIndex >= steps.length - 1) stepIndex = 0;
    else stepIndex++;
    renderThought();
  });

  const renderCard = document.getElementById("renderCard");
  if (renderCard) renderCard.addEventListener("click", openRender);
  const renderAltCard = document.getElementById("renderAltCard");
  if (renderAltCard) renderAltCard.addEventListener("click", openRenderAlt);
  const photoCard = document.getElementById("photoCard");
  if (photoCard) photoCard.addEventListener("click", openPhoto);
  const openModelBtn = document.getElementById("openModelBtn");
  if (openModelBtn) openModelBtn.addEventListener("click", openModel);
  const findUsCtaBtn = document.getElementById("findUsCtaBtn");
  if (findUsCtaBtn) findUsCtaBtn.addEventListener("click", openFindUs);
  const inlineStage = document.getElementById("findUsInlineStage");
  if (inlineStage) mountFindUs(inlineStage);
  const inlineMv = document.getElementById("inlineModelViewer");
  if (inlineMv) {
    inlineMv.addEventListener("dblclick", openModel);
  }
  document.getElementById("inlineModelControls")?.querySelectorAll("[data-view]").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      setView(btn.dataset.view, "inlineModelViewer");
    });
  });
}

function setLeftBg(typeId) {
  document.querySelectorAll(".left-bg-layer").forEach(layer => {
    layer.classList.toggle("on", layer.dataset.bg === typeId);
  });
}

function selectType(id) {
  activeId = id;
  stepIndex = 0;
  setLeftBg(id);
  renderTypeNav();
  renderThought();
}

const FIND_US_PDF = "/media/contact/find-us.pdf";
const FIND_US_QR = [
  { url: "https://metalw-site.vercel.app/ru", label: "01 · Сайт" },
  { url: "https://vizitka-xi.vercel.app/", label: "02 · Производство" },
  { url: "https://alduduk.vercel.app", label: "03 · КБ" },
  { url: "https://metalw.ru", label: "04 · Задача / ТЗ" },
];
let findUsCache = null;
let findUsLoadPromise = null;

function openOverlay(id) { document.getElementById(id).classList.add("open"); document.body.style.overflow = "hidden"; }
function closeOverlay(id) {
  document.getElementById(id).classList.remove("open");
  if (![...document.querySelectorAll(".overlay.open")].length) document.body.style.overflow = "";
}

/** Paint only outer paper margins black — QR white modules stay (not edge-connected). */
function blackoutPaperMargins(ctx, w, h) {
  const img = ctx.getImageData(0, 0, w, h);
  const d = img.data;
  const seen = new Uint8Array(w * h);
  const q = [];
  const isPaper = (i) => {
    const o = i * 4;
    return d[o] > 228 && d[o + 1] > 228 && d[o + 2] > 228;
  };
  const push = (x, y) => {
    if (x < 0 || y < 0 || x >= w || y >= h) return;
    const i = y * w + x;
    if (seen[i] || !isPaper(i)) return;
    seen[i] = 1;
    q.push(i);
  };
  for (let x = 0; x < w; x++) { push(x, 0); push(x, h - 1); }
  for (let y = 0; y < h; y++) { push(0, y); push(w - 1, y); }
  let qi = 0;
  while (qi < q.length) {
    const i = q[qi++];
    const x = i % w;
    const y = (i / w) | 0;
    const o = i * 4;
    d[o] = 10; d[o + 1] = 10; d[o + 2] = 10; d[o + 3] = 255;
    push(x + 1, y); push(x - 1, y); push(x, y + 1); push(x, y - 1);
  }
  ctx.putImageData(img, 0, 0);
}

/** Detect 4 QR blocks (white modules) L→R and map to FIND_US_QR urls. */
function detectQrHotspots(ctx, w, h) {
  const img = ctx.getImageData(0, 0, w, h);
  const d = img.data;
  const y0 = Math.floor(h * 0.52);
  const xMax = Math.floor(w * 0.72);
  const colScore = new Float64Array(w);
  const rowScore = new Float64Array(h);
  for (let y = y0; y < h; y++) {
    for (let x = 0; x < xMax; x++) {
      const o = (y * w + x) * 4;
      if (d[o] > 232 && d[o + 1] > 232 && d[o + 2] > 232) {
        colScore[x] += 1;
        rowScore[y] += 1;
      }
    }
  }
  let yMin = h, yMax = 0;
  for (let y = y0; y < h; y++) {
    if (rowScore[y] > 18) {
      if (y < yMin) yMin = y;
      if (y > yMax) yMax = y;
    }
  }
  if (yMax <= yMin) return null;

  const active = [];
  for (let x = 0; x < xMax; x++) {
    if (colScore[x] > 10) active.push(x);
  }
  if (!active.length) return null;

  const groups = [];
  let s = active[0], prev = active[0];
  for (let i = 1; i < active.length; i++) {
    const x = active[i];
    if (x - prev > 14) {
      groups.push([s, prev]);
      s = x;
    }
    prev = x;
  }
  groups.push([s, prev]);

  // keep 4 widest clusters (QR modules are denser than labels)
  const ranked = groups
    .map(([a, b]) => ({ a, b, w: b - a }))
    .sort((p, q) => q.w - p.w)
    .slice(0, 4)
    .sort((p, q) => p.a - q.a);
  if (ranked.length < 4) return null;

  // pad hit area a bit for labels under QR
  const padX = w * 0.004;
  const padY = h * 0.012;
  const top = Math.max(0, yMin - padY);
  const bottom = Math.min(h, yMax + padY * 2.2);
  return ranked.map((g, i) => {
    const left = Math.max(0, g.a - padX);
    const right = Math.min(w, g.b + padX);
    return {
      url: FIND_US_QR[i].url,
      label: FIND_US_QR[i].label,
      left: (left / w) * 100,
      top: (top / h) * 100,
      width: ((right - left) / w) * 100,
      height: ((bottom - top) / h) * 100,
    };
  });
}

function fallbackQrHotspots() {
  // approximate L→R row if auto-detect fails
  const base = [
    { left: 6.2, top: 71.8, width: 11.2, height: 17.5 },
    { left: 18.4, top: 71.8, width: 11.2, height: 17.5 },
    { left: 30.6, top: 71.8, width: 11.2, height: 17.5 },
    { left: 42.8, top: 71.8, width: 11.2, height: 17.5 },
  ];
  return base.map((b, i) => ({ ...b, url: FIND_US_QR[i].url, label: FIND_US_QR[i].label }));
}

function findUsBarHtml() {
  return FIND_US_QR.map((q) =>
    `<a href="${q.url}" target="_blank" rel="noopener">${q.label}</a>`
  ).join("");
}

async function ensureFindUsRender() {
  if (findUsCache) return findUsCache;
  if (findUsLoadPromise) return findUsLoadPromise;
  findUsLoadPromise = (async () => {
    if (!window.pdfjsLib) throw new Error("pdf.js not loaded");
    pdfjsLib.GlobalWorkerOptions.workerSrc =
      "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
    const pdf = await pdfjsLib.getDocument(FIND_US_PDF).promise;
    const page = await pdf.getPage(1);
    const base = page.getViewport({ scale: 1 });
    const scale = Math.min(2.2, 1600 / base.width);
    const viewport = page.getViewport({ scale });
    const canvas = document.createElement("canvas");
    canvas.width = Math.floor(viewport.width);
    canvas.height = Math.floor(viewport.height);
    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    ctx.fillStyle = "#0a0a0a";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    await page.render({ canvasContext: ctx, viewport }).promise;
    blackoutPaperMargins(ctx, canvas.width, canvas.height);

    const links = detectQrHotspots(ctx, canvas.width, canvas.height) || fallbackQrHotspots();

    findUsCache = {
      dataUrl: canvas.toDataURL("image/jpeg", 0.92),
      width: canvas.width,
      height: canvas.height,
      links,
    };
    return findUsCache;
  })().catch((err) => {
    console.warn("Find-us render failed", err);
    findUsLoadPromise = null;
    return null;
  });
  return findUsLoadPromise;
}

async function mountFindUs(stageEl) {
  if (!stageEl) return;
  stageEl.classList.add("is-loading");
  const data = await ensureFindUsRender();
  const canvas = stageEl.querySelector("canvas");
  const linksEl = stageEl.querySelector(".find-us-links");
  const bar =
    document.getElementById("findUsQrBar") ||
    stageEl.parentElement?.querySelector("[data-find-us-bar], .find-us-qr-bar");
  if (bar) bar.innerHTML = findUsBarHtml();
  if (!data || !canvas || !linksEl) {
    stageEl.classList.remove("is-loading");
    return;
  }
  const img = new Image();
  await new Promise((resolve, reject) => {
    img.onload = resolve;
    img.onerror = reject;
    img.src = data.dataUrl;
  });
  canvas.width = data.width;
  canvas.height = data.height;
  canvas.getContext("2d").drawImage(img, 0, 0);
  linksEl.innerHTML = data.links.map((L) =>
    `<a href="${L.url}" target="_blank" rel="noopener" title="${L.label || ""}" aria-label="${L.label || "QR"}" style="left:${L.left.toFixed(3)}%;top:${L.top.toFixed(3)}%;width:${L.width.toFixed(3)}%;height:${L.height.toFixed(3)}%"></a>`
  ).join("");
  stageEl.classList.remove("is-loading");
}

function openFindUs() {
  openOverlay("findUsOverlay");
  mountFindUs(document.getElementById("findUsStage"));
}
document.getElementById("findUsBtn").addEventListener("click", openFindUs);

function openRender() {
  const t = getType();
  document.getElementById("renderOverlayTitle").textContent = t.renderCaption || t.title;
  const body = document.getElementById("renderOverlayBody");
  body.innerHTML = mediaOrPlaceholder(t.renderCard, t.title);
  hydrateMedia(body);
  openOverlay("renderOverlay");
}

function openPhoto() {
  const t = getType();
  if (!t.renderPhoto) return;
  document.getElementById("renderOverlayTitle").textContent = t.photoCaption || `${t.shortTitle} · фото`;
  const body = document.getElementById("renderOverlayBody");
  body.innerHTML = mediaOrPlaceholder(t.renderPhoto, t.title);
  hydrateMedia(body);
  openOverlay("renderOverlay");
}

function openRenderAlt() {
  const t = getType();
  if (!t.renderCardAlt) return;
  document.getElementById("renderOverlayTitle").textContent = t.renderCaptionAlt || `${t.shortTitle} · render 02`;
  const body = document.getElementById("renderOverlayBody");
  body.innerHTML = mediaOrPlaceholder(t.renderCardAlt, t.title);
  hydrateMedia(body);
  openOverlay("renderOverlay");
}

function openGallery(index = 0) { galleryIndex = index; updateGallery(); openOverlay("galleryOverlay"); }
function updateGallery() {
  const t = getType();
  const g = t.gallery[galleryIndex];
  document.getElementById("galleryOverlayTitle").textContent = `${galleryIndex + 1} / ${t.gallery.length} · ${g.caption}`;
  const media = document.getElementById("galleryOverlayMedia");
  media.innerHTML = mediaOrPlaceholder(g.src, g.caption);
  hydrateMedia(media);
  document.getElementById("galleryOverlayMeta").innerHTML = `<div class="mono" style="color:var(--accent);font-size:10px;margin-bottom:6px">${g.caption}</div>${g.value}`;
}

function openModel() {
  const t = getType();
  document.getElementById("modelOverlayTitle").textContent = t.title;
  document.getElementById("modelOverlayMedia").innerHTML = modelViewerHTML(t, true);
  document.getElementById("modelOverlayControls").innerHTML = Object.keys(VIEWS).map(v => `<button class="btn mono" type="button" data-view="${v}">${v}</button>`).join("");
  document.getElementById("modelOverlayControls").querySelectorAll("[data-view]").forEach(btn => btn.addEventListener("click", () => setView(btn.dataset.view, "fsModelViewer")));
  openOverlay("modelOverlay");
}

function setView(name, viewerId) {
  const mv = document.getElementById(viewerId);
  if (!mv) return;
  mv.setAttribute("camera-orbit", VIEWS[name] || VIEWS.RESET);
}

const appEl = document.getElementById("app");
const fsBtn = document.getElementById("fsToggle");
async function toggleFullscreen() {
  const root = document.documentElement;
  try {
    if (!document.fullscreenElement) {
      await root.requestFullscreen();
      appEl.classList.add("is-fs");
      fsBtn.textContent = "Exit FS";
    } else {
      await document.exitFullscreen();
      appEl.classList.remove("is-fs");
      fsBtn.textContent = "Fullscreen";
    }
  } catch (_) {
    appEl.classList.toggle("is-fs");
    fsBtn.textContent = appEl.classList.contains("is-fs") ? "Exit FS" : "Fullscreen";
  }
}
fsBtn.addEventListener("click", toggleFullscreen);
document.addEventListener("fullscreenchange", () => {
  if (!document.fullscreenElement) {
    appEl.classList.remove("is-fs");
    fsBtn.textContent = "Fullscreen";
  }
});
document.querySelectorAll("[data-close]").forEach(btn => btn.addEventListener("click", () => closeOverlay(btn.dataset.close)));
document.getElementById("galleryPrev").addEventListener("click", () => {
  const t = getType();
  galleryIndex = (galleryIndex - 1 + t.gallery.length) % t.gallery.length;
  updateGallery();
});
document.getElementById("galleryNext").addEventListener("click", () => {
  const t = getType();
  galleryIndex = (galleryIndex + 1) % t.gallery.length;
  updateGallery();
});
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    ["renderOverlay","galleryOverlay","modelOverlay","findUsOverlay"].forEach(closeOverlay);
    if (demoPlaying) stopDemo();
  }
  const anyOpen = [...document.querySelectorAll(".overlay.open")].length;
  if (!anyOpen) {
    if (e.key === "ArrowRight") { e.preventDefault(); document.getElementById("nextStep")?.click(); }
    if (e.key === "ArrowLeft") { e.preventDefault(); document.getElementById("prevStep")?.click(); }
    if (e.key === " ") { e.preventDefault(); toggleDemo(); }
  }
  if (document.getElementById("galleryOverlay").classList.contains("open")) {
    if (e.key === "ArrowLeft") document.getElementById("galleryPrev").click();
    if (e.key === "ArrowRight") document.getElementById("galleryNext").click();
  }
});

/* Demo mode: auto-play all types/steps (+ music/pulse optional) */
let demoPlaying = false;
let demoWithAudio = false;
let demoAdvancing = false;
let demoTimer = null;
let demoPlaylist = [];
let demoPos = 0;
const demoAudio = document.getElementById("demoAudio");
const demoBtn = document.getElementById("demoToggle");
const demoIcon = document.getElementById("demoIcon");
const demoLabel = document.getElementById("demoLabel");
const demoQuietBtn = document.getElementById("demoQuietToggle");
const demoQuietIcon = document.getElementById("demoQuietIcon");
const demoQuietLabel = document.getElementById("demoQuietLabel");

function buildDemoPlaylist() {
  const list = [];
  TYPES.forEach((t) => {
    stepsFor(t).forEach((step, i) => {
      list.push({ typeId: t.id, stepIndex: i, kind: step.kind });
    });
  });
  return list;
}

function stepDuration(kind) {
  if (kind === "model") return 7500;
  if (kind === "render" || kind === "renderAlt" || kind === "photo") return 6500;
  if (kind === "cta") return 5500;
  return 5200;
}

function updateDemoBtn() {
  const pulseOn = demoPlaying && demoWithAudio;
  const quietOn = demoPlaying && !demoWithAudio;
  demoBtn.classList.toggle("is-playing", pulseOn);
  demoIcon.textContent = pulseOn ? "❚❚" : "▶";
  demoLabel.textContent = pulseOn ? "Stop" : "Demo";
  demoQuietBtn.classList.toggle("is-playing", quietOn);
  demoQuietIcon.textContent = quietOn ? "❚❚" : "▶";
  demoQuietLabel.textContent = quietOn ? "Stop" : "Auto";
}

function demoGoTo(pos) {
  const item = demoPlaylist[pos];
  if (!item) return;
  demoAdvancing = true;
  activeId = item.typeId;
  stepIndex = item.stepIndex;
  setLeftBg(activeId);
  renderTypeNav();
  renderThought();
  demoAdvancing = false;
}

function demoTick() {
  demoPos += 1;
  if (demoPos >= demoPlaylist.length) {
    stopDemo(true);
    return;
  }
  demoGoTo(demoPos);
  const item = demoPlaylist[demoPos];
  demoTimer = setTimeout(demoTick, stepDuration(item.kind));
}

const DEMO_AUDIO_URL = "/media/audio/metalwork-pulse.mp3";
let audioCtx = null;
let analyser = null;
let beatRaf = null;
let beatFreq = null;
let beatTime = null;
let beatSmooth = 0;
let beatPeak = 0.02;
let musicBuffer = null;
let musicSource = null;
let musicGain = null;
let musicLoadPromise = null;
let useElementFallback = false;

function getAudioCtx() {
  const Ctx = window.AudioContext || window.webkitAudioContext;
  if (!Ctx) return null;
  audioCtx = audioCtx || new Ctx();
  return audioCtx;
}

function wireAnalyser(ctx) {
  if (analyser) return;
  analyser = ctx.createAnalyser();
  analyser.fftSize = 1024;
  analyser.smoothingTimeConstant = 0.35;
  analyser.minDecibels = -90;
  analyser.maxDecibels = -10;
  beatFreq = new Uint8Array(analyser.frequencyBinCount);
  beatTime = new Uint8Array(analyser.fftSize);
  musicGain = ctx.createGain();
  musicGain.gain.value = 0.72;
  musicGain.connect(analyser);
  analyser.connect(ctx.destination);
}

async function loadMusicBuffer() {
  if (musicBuffer) return musicBuffer;
  if (musicLoadPromise) return musicLoadPromise;
  musicLoadPromise = (async () => {
    const ctx = getAudioCtx();
    if (!ctx) throw new Error("no AudioContext");
    wireAnalyser(ctx);
    const res = await fetch(DEMO_AUDIO_URL);
    if (!res.ok) throw new Error("audio fetch " + res.status);
    const raw = await res.arrayBuffer();
    musicBuffer = await ctx.decodeAudioData(raw.slice(0));
    return musicBuffer;
  })().catch((err) => {
    console.warn("Music buffer failed, element fallback", err);
    musicLoadPromise = null;
    return null;
  });
  return musicLoadPromise;
}

function stopMusicSource() {
  if (musicSource) {
    try { musicSource.stop(0); } catch (_) {}
    try { musicSource.disconnect(); } catch (_) {}
    musicSource = null;
  }
}

async function startMusic() {
  const ctx = getAudioCtx();
  if (!ctx) {
    useElementFallback = true;
    return playElementFallback();
  }
  try {
    if (ctx.state === "suspended") await ctx.resume();
  } catch (_) {}

  const buf = await loadMusicBuffer();
  if (!buf || !musicGain) {
    useElementFallback = true;
    return playElementFallback();
  }

  useElementFallback = false;
  stopMusicSource();
  if (demoAudio) {
    try { demoAudio.pause(); } catch (_) {}
  }

  musicSource = ctx.createBufferSource();
  musicSource.buffer = buf;
  musicSource.loop = true;
  musicSource.connect(musicGain);
  musicSource.start(0);
}

async function playElementFallback() {
  const ctx = getAudioCtx();
  if (ctx && demoAudio && !analyser) {
    try {
      wireAnalyser(ctx);
      const src = ctx.createMediaElementSource(demoAudio);
      src.connect(musicGain);
      if (ctx.state === "suspended") await ctx.resume();
    } catch (err) {
      console.warn("Element analyser failed", err);
    }
  }
  if (!demoAudio) return;
  demoAudio.currentTime = 0;
  demoAudio.volume = 0.7;
  try { await demoAudio.play(); } catch (_) {}
}

function stopMusic() {
  stopMusicSource();
  if (demoAudio) {
    demoAudio.pause();
    demoAudio.currentTime = 0;
  }
}

let beatPrev = 0;
let glitchUntil = 0;

function beatLoop() {
  if (!demoPlaying) return;

  let raw = 0;
  if (analyser && beatFreq && beatTime) {
    analyser.getByteFrequencyData(beatFreq);
    analyser.getByteTimeDomainData(beatTime);

    let bass = 0;
    for (let i = 0; i < 24; i++) bass = Math.max(bass, beatFreq[i] || 0);
    bass /= 255;

    let energy = 0;
    for (let i = 0; i < beatFreq.length; i++) energy += beatFreq[i] || 0;
    energy = energy / beatFreq.length / 255;

    let rms = 0;
    for (let i = 0; i < beatTime.length; i++) {
      const v = (beatTime[i] - 128) / 128;
      rms += v * v;
    }
    rms = Math.sqrt(rms / beatTime.length);

    // punchier on transients / bass
    raw = Math.max(bass * 1.75, energy * 2.1, rms * 5.2);
    if (raw < 0.04) {
      const t = performance.now() / 1000;
      raw = 0.55 + 0.4 * Math.pow(0.5 + 0.5 * Math.sin(t * Math.PI * 2.35), 12);
    } else {
      beatPeak = Math.max(beatPeak * 0.992, raw, 0.07);
      raw = Math.min(1, raw / beatPeak);
    }
  } else {
    const t = performance.now() / 1000;
    raw = 0.55 + 0.4 * Math.pow(0.5 + 0.5 * Math.sin(t * Math.PI * 2.35), 12);
  }

  // attack bias — kicks hit harder, release a bit slower
  const attack = raw > beatSmooth ? 0.82 : 0.28;
  beatSmooth = beatSmooth * (1 - attack) + raw * attack;
  const pulse = Math.min(1, Math.max(0, beatSmooth));
  const now = performance.now();

  // light glitch on strong onsets (overlay only — no layout shift)
  const onset = pulse - beatPrev;
  beatPrev = pulse;
  if (onset > 0.14 && pulse > 0.42) {
    glitchUntil = now + 45 + Math.random() * 50;
  } else if (pulse > 0.78 && Math.random() < 0.03) {
    glitchUntil = now + 30 + Math.random() * 40;
  }

  const glitching = now < glitchUntil;
  document.body.classList.toggle("is-glitching", glitching);

  let rgb = 0, scan = pulse * 0.25;
  if (glitching) {
    rgb = 0.4 + pulse * 0.9;
    scan = 0.4 + pulse * 0.5;
  } else if (pulse > 0.55) {
    rgb = pulse * 0.3;
  }

  const root = document.documentElement.style;
  root.setProperty("--beat", pulse.toFixed(3));
  // backgrounds only — keep modest so media doesn't feel "stretched"
  root.setProperty("--beat-scale", (1 + pulse * 0.028).toFixed(4));
  root.setProperty("--glitch-x", "0px");
  root.setProperty("--glitch-y", "0px");
  root.setProperty("--glitch-skew", "0deg");
  root.setProperty("--glitch-rgb", rgb.toFixed(2));
  root.setProperty("--glitch-scan", scan.toFixed(2));
  beatRaf = requestAnimationFrame(beatLoop);
}

function resetBeatVars() {
  const root = document.documentElement.style;
  root.setProperty("--beat", "0");
  root.setProperty("--beat-scale", "1");
  root.setProperty("--glitch-x", "0px");
  root.setProperty("--glitch-y", "0px");
  root.setProperty("--glitch-skew", "0deg");
  root.setProperty("--glitch-rgb", "0");
  root.setProperty("--glitch-scan", "0");
}

function startBeatPulse() {
  document.body.classList.add("is-demo-beat");
  document.body.classList.remove("is-glitching");
  cancelAnimationFrame(beatRaf);
  beatSmooth = 0.25;
  beatPrev = 0;
  beatPeak = 0.02;
  glitchUntil = 0;
  beatRaf = requestAnimationFrame(beatLoop);
}

function stopBeatPulse() {
  cancelAnimationFrame(beatRaf);
  beatRaf = null;
  beatSmooth = 0;
  beatPrev = 0;
  glitchUntil = 0;
  document.body.classList.remove("is-demo-beat", "is-glitching");
  resetBeatVars();
}

function startDemo(withAudio) {
  if (demoPlaying) stopDemo(false);
  demoPlaylist = buildDemoPlaylist();
  if (!demoPlaylist.length) return;
  demoPos = 0;
  demoPlaying = true;
  demoWithAudio = !!withAudio;
  updateDemoBtn();
  demoGoTo(0);
  if (demoWithAudio) {
    startBeatPulse();
    startMusic().catch(() => {});
  }
  demoTimer = setTimeout(demoTick, stepDuration(demoPlaylist[0].kind));
}

function stopDemo(finished) {
  demoPlaying = false;
  demoWithAudio = false;
  if (demoTimer) clearTimeout(demoTimer);
  demoTimer = null;
  stopBeatPulse();
  stopMusic();
  updateDemoBtn();
}

function toggleDemo() {
  if (demoPlaying && demoWithAudio) stopDemo(false);
  else startDemo(true);
}

function toggleQuietDemo() {
  if (demoPlaying && !demoWithAudio) stopDemo(false);
  else startDemo(false);
}

demoBtn.addEventListener("click", toggleDemo);
demoQuietBtn.addEventListener("click", toggleQuietDemo);
// warm-decode track so first Demo click pulses immediately
loadMusicBuffer().catch(() => {});

/* PDF export: all slides in order, NO 3D models */
function buildPdfPlaylist() {
  const list = [];
  TYPES.forEach((t) => {
    stepsFor(t).forEach((step, i) => {
      if (step.kind === "model") return; // модели в PDF не тащим
      list.push({ type: t, step, stepIndex: i });
    });
  });
  return list;
}

function pdfTitleHtml(lines) {
  return (lines || []).map((line, i) => {
    const last = i === lines.length - 1;
    return i === 0
      ? (last ? `<span class="acc">${line}</span>` : line)
      : `<br><span class="${last ? "acc" : ""}">${line}</span>`;
  }).join("");
}

function buildPdfPage(item, index, total) {
  const t = item.type;
  const s = item.step;
  const n = String(index + 1).padStart(2, "0");
  const tot = String(total).padStart(2, "0");
  const bg = s.kind === "text" || s.kind === "cta"
    ? resolveStepBackground(t, s.key)
    : (s.kind === "photo" ? t.renderPhoto : (s.kind === "renderAlt" ? t.renderCardAlt : t.renderCard));
  const speaker = speakerForStep(t, s);

  let content = "";
  if (s.kind === "text") {
    content = `
      <h2 class="pdf-title">${pdfTitleHtml(s.title)}</h2>
      ${s.body ? `<div class="pdf-body">${s.body}</div>` : ""}`;
  } else if (s.kind === "cta") {
    content = `
      <h2 class="pdf-title">Покажите<br><span class="acc">проблемную операцию.</span></h2>
      <div class="pdf-body">Разберём, где теряется управление — и какой оснасткой вернуть ритм.</div>`;
  } else if (s.kind === "render" || s.kind === "renderAlt" || s.kind === "photo") {
    const src = s.kind === "photo" ? t.renderPhoto : (s.kind === "renderAlt" ? t.renderCardAlt : t.renderCard);
    const label = s.kind === "photo" ? "Photo · shop floor" : (s.kind === "renderAlt" ? "Render · concept 02" : "Render · concept");
    const callouts = (t.callouts || []).slice(0, 6).map(([a]) => `<span>${a}</span>`).join("");
    const metrics = (t.metrics || []).slice(0, 4).map(([a, b]) => `<div><b>${a}</b><span>${b}</span></div>`).join("");
    content = `
      <h2 class="pdf-title">${t.shortTitle}</h2>
      <div class="pdf-media"><img src="${src}" alt="${t.title}" /></div>
      ${s.kind !== "photo" ? `<div class="pdf-callouts">${callouts}</div><div class="pdf-metrics">${metrics}</div>` : `<div class="pdf-body" style="margin-top:14px">${t.photoCaption || "Живое фото установки"}</div>`}
      <div class="pdf-meta" style="margin-top:12px">${label}</div>`;
  }

  const speakerBlock = speaker
    ? `<aside class="pdf-speaker">
        <div class="pdf-speaker-label">Speaker · речь</div>
        <p class="pdf-speaker-text">${speaker}</p>
      </aside>`
    : "";

  return `<section class="pdf-page ${speaker ? "has-speaker" : ""}">
    ${bg ? `<div class="pdf-page-bg" style="background-image:url('${bg}')"></div><div class="pdf-page-veil"></div>` : ""}
    <div class="pdf-page-inner">
      <p class="pdf-kicker">Metalwork Pulse · DIR-01 · ${t.shortTitle}</p>
      <p class="pdf-meta">${n} / ${tot} · ${s.slug}</p>
      ${content}
      ${speakerBlock}
    </div>
  </section>`;
}

function openPdfExport() {
  stopDemo(false);
  const list = buildPdfPlaylist();
  const root = document.getElementById("pdfRoot");
  if (!list.length) {
    alert("Нет слайдов для PDF");
    return;
  }
  root.innerHTML = `
    <div class="pdf-toolbar">
      <div class="mono" style="color:#b8ff3e;font-size:11px;letter-spacing:.18em;text-transform:uppercase">PDF · ${list.length} слайдов · без 3D · по центру экрана</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-primary" type="button" id="pdfPrintBtn">Печать / Save PDF</button>
        <button class="btn btn-ghost" type="button" id="pdfCloseBtn">Назад</button>
      </div>
    </div>
    ${list.map((item, i) => buildPdfPage(item, i, list.length)).join("")}
  `;
  document.documentElement.classList.add("pdf-export");
  document.body.classList.add("pdf-export");
  root.setAttribute("aria-hidden", "false");
  window.scrollTo(0, 0);

  document.getElementById("pdfPrintBtn").addEventListener("click", () => window.print());
  document.getElementById("pdfCloseBtn").addEventListener("click", closePdfExport);
}

function closePdfExport() {
  document.documentElement.classList.remove("pdf-export");
  document.body.classList.remove("pdf-export");
  const root = document.getElementById("pdfRoot");
  root.innerHTML = "";
  root.setAttribute("aria-hidden", "true");
}

document.getElementById("pdfExport").addEventListener("click", openPdfExport);

function stripQuery(url) {
  return (url || "").split("?")[0];
}

async function imageToDataUrl(url) {
  const meta = await loadImageMeta(url);
  return meta ? meta.dataUrl : null;
}

async function loadImageMeta(url) {
  if (!url) return null;
  const clean = stripQuery(url);
  try {
    const res = await fetch(clean);
    if (!res.ok) return null;
    const blob = await res.blob();
    const dataUrl = await new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
    const dims = await new Promise((resolve) => {
      const img = new Image();
      img.onload = () => resolve({ w: img.naturalWidth || img.width, h: img.naturalHeight || img.height });
      img.onerror = () => resolve({ w: 0, h: 0 });
      img.src = dataUrl;
    });
    if (!dims.w || !dims.h) return null;
    return { dataUrl, w: dims.w, h: dims.h };
  } catch (_) {
    return null;
  }
}

/** Fit image into box (inches), keep aspect ratio, center. */
function fitImageBox(imgW, imgH, boxX, boxY, boxW, boxH) {
  const ar = imgW / imgH;
  const boxAr = boxW / boxH;
  let w, h;
  if (ar > boxAr) {
    w = boxW;
    h = boxW / ar;
  } else {
    h = boxH;
    w = boxH * ar;
  }
  return {
    x: boxX + (boxW - w) / 2,
    y: boxY + (boxH - h) / 2,
    w,
    h,
  };
}

function plainTitle(lines) {
  return (lines || []).join(" ");
}

async function exportPptx() {
  stopDemo(false);
  const PptxGenJS = window.PptxGenJS;
  if (!PptxGenJS) {
    alert("PptxGenJS не загрузился. Проверь интернет (CDN) и обнови страницу.");
    return;
  }

  const btn = document.getElementById("pptxExport");
  const prev = btn.textContent;
  btn.textContent = "PPTX…";
  btn.disabled = true;

  try {
    const list = buildPdfPlaylist(); // без model
    const pptx = new PptxGenJS();
    pptx.defineLayout({ name: "MW_WIDE", width: 13.333, height: 7.5 });
    pptx.layout = "MW_WIDE";
    pptx.author = "Metalwork Pulse";
    pptx.title = "Metalwork Pulse · DIR-01";

    for (let i = 0; i < list.length; i++) {
      const { type: t, step: s } = list[i];
      const slide = pptx.addSlide();
      slide.background = { color: "0A0A0A" };

      const n = String(i + 1).padStart(2, "0");
      const tot = String(list.length).padStart(2, "0");

      slide.addText(`METALWORK PULSE · DIR-01 · ${t.shortTitle.toUpperCase()}`, {
        x: 0.5, y: 0.28, w: 12.3, h: 0.3,
        fontSize: 11, fontFace: "Arial", color: "B8FF3E",
        charSpacing: 4,
      });
      slide.addText(`${n} / ${tot}  ·  ${s.slug}`, {
        x: 0.5, y: 0.55, w: 12.3, h: 0.25,
        fontSize: 10, fontFace: "Arial", color: "8A8680",
      });

      if (s.kind === "text") {
        slide.addText(plainTitle(s.title), {
          x: 0.5, y: 1.3, w: 11.5, h: 2.2,
          fontSize: 36, fontFace: "Arial", color: "F4F1EA", bold: true,
          valign: "top",
        });
        if (s.body) {
          slide.addText(s.body, {
            x: 0.5, y: 3.7, w: 10, h: 2.4,
            fontSize: 16, fontFace: "Arial", color: "C8C4BB",
            valign: "top",
          });
        }
      } else if (s.kind === "cta") {
        slide.addText("Покажите проблемную операцию.", {
          x: 0.5, y: 2.2, w: 12, h: 1.4,
          fontSize: 36, fontFace: "Arial", color: "B8FF3E", bold: true,
        });
        slide.addText("Разберём, где теряется управление — и какой оснасткой вернуть ритм.", {
          x: 0.5, y: 3.8, w: 10, h: 1.2,
          fontSize: 16, fontFace: "Arial", color: "C8C4BB",
        });
      } else {
        const src = s.kind === "photo"
          ? t.renderPhoto
          : (s.kind === "renderAlt" ? t.renderCardAlt : t.renderCard);
        const meta = await loadImageMeta(src);
        slide.addText(t.shortTitle, {
          x: 0.5, y: 0.95, w: 12, h: 0.45,
          fontSize: 22, fontFace: "Arial", color: "F4F1EA", bold: true,
        });
        if (meta) {
          const box = fitImageBox(meta.w, meta.h, 1.2, 1.55, 10.9, 4.6);
          slide.addImage({
            data: meta.dataUrl,
            x: box.x,
            y: box.y,
            w: box.w,
            h: box.h,
          });
        } else {
          slide.addText("Image unavailable", {
            x: 0.5, y: 3, w: 12, h: 0.4,
            fontSize: 14, color: "8A8680",
          });
        }
      }
    }

    await pptx.writeFile({ fileName: "Metalwork-Pulse-DIR-01.pptx" });
  } catch (err) {
    console.error(err);
    alert("Не удалось собрать PPTX. Смотри console.");
  } finally {
    btn.textContent = prev;
    btn.disabled = false;
  }
}

document.getElementById("pptxExport").addEventListener("click", exportPptx);

/* Premium: cursor + flashlight + parallax */
(function premiumMotion() {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(pointer: fine)").matches;
  if (reduce || !fine) return;

  const dot = document.getElementById("cursorDot");
  let mx = window.innerWidth / 2;
  let my = window.innerHeight / 2;

  function onMove(e) {
    mx = e.clientX;
    my = e.clientY;
    document.documentElement.style.setProperty("--mx", mx + "px");
    document.documentElement.style.setProperty("--my", my + "px");
    if (dot) dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%,-50%)`;

    const cx = window.innerWidth / 2;
    const cy = window.innerHeight / 2;
    const dx = (mx - cx) / cx;
    const dy = (my - cy) / cy;

    document.querySelectorAll(".parallax-title").forEach(el => {
      el.style.transform = `translate3d(${dx * 14}px, ${dy * 10}px, 0)`;
    });
    document.querySelectorAll(".parallax-glass").forEach(el => {
      el.style.transform = `translate3d(${dx * -10}px, ${dy * -8}px, 0)`;
    });
    document.querySelectorAll(".parallax-meta").forEach(el => {
      el.style.transform = `translate3d(${dx * 6}px, ${dy * 4}px, 0)`;
    });
    document.querySelectorAll(".left .stack").forEach(el => {
      el.style.transform = `translate3d(${dx * 8}px, ${dy * 6}px, 0)`;
    });
    document.querySelectorAll(".left-bg-layer.on").forEach(el => {
      el.style.transform = `scale(1.08) translate3d(${dx * -12}px, ${dy * -10}px, 0)`;
    });
  }

  window.addEventListener("mousemove", onMove, { passive: true });
})();

try { localStorage.removeItem("mw-pulse-theme"); } catch (_) {}
setLeftBg(activeId);
renderTypeNav();
renderThought();
updateDemoBtn();
</script>
</body>
</html>
'''

def main():
    content = HTML_HEAD + TYPES_JS + HTML_TAIL
    for out in OUTS:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"wrote {out} ({out.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
