import type { AtlasGraph, AtlasNodeContent, AtlasSubnode } from "./atlas-types";
import { clampingFixturesSubnodes } from "./clamping-subnodes";

export const atlasGraph: AtlasGraph = {
  manifesto: {
    headline: "ОТК не предотвращает брак.",
    subline: "Он фиксирует убытки.",
    editorialSubline:
      "Брак рождается раньше — в операции, которая оставила ошибке место.",
    productTitle: "METALWORK",
    productPulse: "MW PULSE",
    pulseLead:
      "Реанимация для ваших больных производственных вопросов: находим место, где операция теряет управление, и возвращаем процессу ритм.",
    centerTitle: "METALWORK PULSE",
    centerTagline:
      "Мы не продаём железо. Мы проектируем физический запрет на ошибку.",
    exploreLabel: "Recovery Modules →",
  },
  nodes: [
    {
      id: "metalwork",
      title: "METALWORK PULSE",
      type: "root",
      summary:
        "Диагностика производственных операций: где процесс теряет управление, и каким инженерным решением вернуть ему ритм.",
      strongPhrase:
        "Мы не продаём железо. Мы проектируем физический запрет на ошибку.",
      purpose:
        "Инженерная система диагностики и восстановления ритма производственных операций Metalwork.",
      children: [
        "clamping-fixtures",
        "welding-fixtures",
        "assembly-fixtures",
        "part-flippers",
        "lifting-rigging",
        "aggregate-machines",
        "custom-equipment",
        "reverse-engineering",
        "inspection-fixtures",
        "manual-op-mechanization",
      ],
    },
    {
      id: "clamping-fixtures",
      ref: "DIR-01",
      title: "Станочная зажимная оснастка",
      shortTitle: "Зажимная",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Инженерная система базирования, упора и зажима детали, которая превращает ручную установку в повторяемый процесс.",
      strongPhrase:
        "Если деталь физически можно поставить криво — рано или поздно её поставят криво.",
      purpose:
        "Убрать неопределённость установки до первого реза. Сделать правильное положение детали единственным возможным.",
      painPoints: [
        "Ручная выверка на каждой партии",
        "Подкладки и перезажим",
        "Риск перекоса и смещения детали",
        "Зависимость результата от смены и оператора",
        "Нестабильное время установки",
        "Прижим «по ощущениям»",
        "Брак, который рождается в установке, а не в резании",
      ],
      solutionTypes: [
        {
          title: "Механическая",
          description: "Простота, жёсткость, ремонтопригодность.",
          whenToUse: "Стабильная геометрия, умеренные усилия, серийность.",
          whenNotToUse: "Нужна высокая скорость переналадки без механического вмешательства.",
        },
        {
          title: "Пневматическая",
          description: "Скорость, повторяемая последовательность, меньше ручных действий.",
          whenToUse: "Частая переналадка, такт важнее максимального усилия.",
          whenNotToUse: "Нет стабильного воздуха или нужны большие усилия без гидравлики.",
        },
        {
          title: "Гидравлическая",
          description: "Стабильное усилие на ответственных деталях.",
          whenToUse: "Высокие усилия зажима, ответственная геометрия.",
          whenNotToUse: "Медленный цикл или риск загрязнения гидросистемы в цехе.",
        },
        {
          title: "Модульная",
          description: "Быстрая переналадка под разные партии.",
          whenToUse: "Семейство деталей, частая смена номенклатуры.",
          whenNotToUse: "Одна деталь на годы — избыточная сложность.",
        },
        {
          title: "Специальная",
          description: "Максимум точности под конкретную операцию.",
          whenToUse: "Жёсткие допуски, нестандартная геометрия, узкий такт.",
          whenNotToUse: "Универсальная наладка важнее точности под одну операцию.",
        },
      ],
      whereUsed: [
        "Фрезерная и токарная обработка серийных деталей",
        "Операции с жёсткими допусками на базирование",
        "Участки, где наладка дольше цикла резания",
        "Производство, где смена оператора не должна менять результат",
      ],
      whenNotUsed: [
        "Когда деталь уже имеет жёсткую базу в самой заготовке без оснастки",
        "Когда объём единичный и экономика оснастки не сходится",
        "Когда проблема в программе или инструменте, а не в установке",
      ],
      questions: [
        "Сколько минут уходит на установку до первого реза?",
        "Где оператор «чувствует» положение, а не фиксирует его?",
        "Что происходит при смене партии или оператора?",
        "Где деталь физически может встать криво — и кто это заметит?",
        "Сколько станочных часов в месяц уходит не на резание?",
      ],
      requiredInput: [
        "Чертёж или 3D-модель детали",
        "Допуски на базирование и припуски",
        "Схема обработки и доступ инструмента",
        "Такт операции и объём партии",
        "Тип станка и размеры стола",
        "Усилия зажима и требования к деформации",
      ],
      mediaPlan: [
        {
          type: "cad",
          title: "CAD-like viewer",
          description: "BASE · STOP · CLAMP · SUPPORT · FIXTURE PLATE",
          placeholder: true,
        },
        {
          type: "photo",
          title: "Фото оснастки в цехе",
          placeholder: true,
        },
        {
          type: "drawing",
          title: "Схема базирования",
          placeholder: true,
        },
      ],
      cta: {
        label: "Показать проблемную операцию",
        description:
          "Покажите операцию, которую пора перестать терпеть — разберём и покажем, какой оснасткой закрыть риск.",
        href: "mailto:contact@metalwork.example?subject=Проблемная%20операция%20—%20DIR-01",
      },
      directionRoute: "/directions/clamping-fixtures",
      presentRoute: "/present/clamping-fixtures",
      subnodes: clampingFixturesSubnodes,
    },
    {
      id: "welding-fixtures",
      ref: "DIR-02",
      title: "Сварочная оснастка",
      shortTitle: "Сварка",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Позиционирование и фиксация под сварку — когда шов зависит от повторяемости, а не от глазомера.",
      strongPhrase:
        "Геометрия изделия должна жить в стапеле, а не в глазомере.",
    },
    {
      id: "assembly-fixtures",
      title: "Сборочная оснастка",
      shortTitle: "Сборка",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Сборка без перекоса — когда узел должен сойтись одинаково в каждой единице.",
      strongPhrase: "Сборка — это последовательность допусков, а не интуиция.",
    },
    {
      id: "part-flippers",
      ref: "DIR-03",
      title: "Кантователи",
      shortTitle: "Кантователи",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Переворот и позиционирование тяжёлых деталей без ручного героизма и риска травмы.",
      strongPhrase:
        "Кран должен поднимать, а не изображать технологический процесс.",
    },
    {
      id: "lifting-rigging",
      title: "Подъёмные и монтажные приспособления",
      shortTitle: "Подъём",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Безопасный захват, подъём и установка — когда вес и геометрия не прощают импровизации.",
      strongPhrase: "Если захват не рассчитан — операция держится на удаче.",
    },
    {
      id: "aggregate-machines",
      ref: "DIR-04",
      title: "Агрегатные станки",
      shortTitle: "Агрегаты",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Специализированное оборудование под операцию — когда универсальный станок проигрывает по такту и точности.",
      strongPhrase:
        "Повторяемую операцию пора превращать в отдельную машину.",
    },
    {
      id: "custom-equipment",
      title: "Нестандартное оборудование",
      shortTitle: "Нестандарт",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Инженерные решения вне каталога — когда задача не укладывается в типовую машину.",
      strongPhrase:
        "Нестандарт — это не хаос, а расчёт под конкретную физику процесса.",
    },
    {
      id: "reverse-engineering",
      title: "Реверс-инжиниринг",
      shortTitle: "Реверс",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Восстановление геометрии и технологии по образцу — когда чертежа нет, а деталь нужна.",
      strongPhrase: "Образец — не чертёж, но инженерный объект для анализа.",
    },
    {
      id: "inspection-fixtures",
      title: "Контрольные приспособления",
      shortTitle: "Контроль",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Измерение и проверка в оснастке — когда ОТК должен быть быстрым, а не постфактумным.",
      strongPhrase: "ОТК не предотвращает брак. Он фиксирует убытки.",
    },
    {
      id: "manual-op-mechanization",
      title: "Механизация ручных операций",
      shortTitle: "Механизация",
      type: "direction",
      parentId: "metalwork",
      summary:
        "Убираем ручной труд там, где он создаёт вариативность, усталость и брак.",
      strongPhrase: "Рука устаёт раньше, чем заканчивается смена.",
    },
  ],
};

const nodeMap = new Map(
  atlasGraph.nodes.map((node) => [node.id, node]),
);

export function getAtlasNode(id: string): AtlasNodeContent | undefined {
  return nodeMap.get(id);
}

export function getAtlasDirections(): AtlasNodeContent[] {
  return atlasGraph.nodes.filter((n) => n.type === "direction");
}

export function getAtlasRoot(): AtlasNodeContent {
  return atlasGraph.nodes.find((n) => n.type === "root")!;
}

export function getAtlasSubnode(
  directionId: string,
  subnodeId: string,
): AtlasSubnode | undefined {
  const direction = getAtlasNode(directionId);
  return direction?.subnodes?.find((s) => s.id === subnodeId);
}

export type DossierTarget =
  | { kind: "direction"; direction: AtlasNodeContent }
  | { kind: "subnode"; direction: AtlasNodeContent; subnode: AtlasSubnode };

export function resolveDossier(
  directionId: string | null,
  subnodeId: string | null,
): DossierTarget | null {
  if (!directionId) return null;
  const direction = getAtlasNode(directionId);
  if (!direction) return null;
  if (subnodeId) {
    const subnode = getAtlasSubnode(directionId, subnodeId);
    if (subnode) return { kind: "subnode", direction, subnode };
  }
  return { kind: "direction", direction };
}

/** CAD callout labels for DIR-01 media slot */
export const clampingFixturesCadLabels = [
  { id: "base", label: "BASE", description: "задаёт положение детали.", x: 22, y: 78 },
  { id: "stop", label: "STOP", description: "не даёт детали уйти.", x: 78, y: 42 },
  { id: "clamp", label: "CLAMP", description: "удерживает с понятным усилием.", x: 72, y: 28 },
  { id: "support", label: "SUPPORT", description: "убирает прогиб и вибрацию.", x: 50, y: 62 },
  { id: "fixture-plate", label: "FIXTURE PLATE", description: "собирает операцию в одну систему.", x: 38, y: 48 },
];
