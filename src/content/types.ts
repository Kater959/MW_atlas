export type SlideType =
  | "hook"
  | "pain"
  | "before-after"
  | "solution-logic"
  | "cad-viewer"
  | "cta";

export interface DirectionMeta {
  id: string;
  ref: string;
  label: string;
  titleRu: string;
  slug: string;
}

export interface HookSlideContent {
  type: "hook";
  id: string;
  title: string;
  subtitle: string;
  bullets: string[];
}

export interface PainSlideContent {
  type: "pain";
  id: string;
  title: string;
  subtitle: string;
  bullets: string[];
}

export interface BeforeAfterSlideContent {
  type: "before-after";
  id: string;
  title: string;
  afterTitle: string;
  before: string[];
  after: string[];
}

export interface SolutionLogicNode {
  id: string;
  title: string;
  description: string;
}

export interface SolutionLogicSlideContent {
  type: "solution-logic";
  id: string;
  title: string;
  subtitle: string;
  nodes: SolutionLogicNode[];
  footer: string;
}

export interface CadNodeLabel {
  id: string;
  label: string;
  description: string;
  x: number;
  y: number;
}

export interface CadViewerSlideContent {
  type: "cad-viewer";
  id: string;
  title: string;
  subtitle: string;
  nodes: CadNodeLabel[];
  viewerFooter: string;
  slideFooter: string;
}

export interface CtaSlideContent {
  type: "cta";
  id: string;
  title: string;
  subtitle: string;
  bullets: string[];
  primary: { label: string; href: string };
  secondaryText: string;
}

export type SlideContent =
  | HookSlideContent
  | PainSlideContent
  | BeforeAfterSlideContent
  | SolutionLogicSlideContent
  | CadViewerSlideContent
  | CtaSlideContent;

export interface DirectionDeck {
  meta: DirectionMeta;
  slides: SlideContent[];
}

export type CadViewAngle = "front" | "top" | "iso";
