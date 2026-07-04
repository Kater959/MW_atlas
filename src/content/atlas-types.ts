export type AtlasNodeType =
  | "root"
  | "direction"
  | "solution"
  | "pain"
  | "media"
  | "question";

export type AtlasSubnodeType =
  | "solutionType"
  | "pain"
  | "data"
  | "whereUsed"
  | "cad"
  | "media";

export interface AtlasVisualCallout {
  label: string;
  description?: string;
}

export interface AtlasVisual {
  id?: string;
  type: "render" | "image" | "photo" | "model" | "sketch" | "drawing";
  title: string;
  src: string;
  label?: string;
  subtitle?: string;
  poster?: string;
  caption?: string;
  callouts?: AtlasVisualCallout[];
}

export interface AtlasSubnode {
  id: string;
  title: string;
  type: AtlasSubnodeType;
  strongPhrase?: string;
  summary?: string;
  purpose?: string;
  whereUsed?: string[];
  whenToUse?: string[];
  whenNotToUse?: string[];
  advantages?: string[];
  risks?: string[];
  questions?: string[];
  requiredInput?: string[];
  painPoints?: string[];
  visuals?: AtlasVisual[];
}

export interface AtlasCta {
  label: string;
  description?: string;
  href?: string;
}

export interface AtlasSolutionType {
  title: string;
  description: string;
  whenToUse?: string;
  whenNotToUse?: string;
}

export interface AtlasMediaPlan {
  type: "photo" | "sketch" | "drawing" | "render" | "video" | "cad";
  title: string;
  description?: string;
  placeholder?: boolean;
}

export interface AtlasNodeContent {
  id: string;
  title: string;
  shortTitle?: string;
  type: AtlasNodeType;
  summary: string;
  strongPhrase?: string;
  purpose?: string;
  parentId?: string | null;
  children?: string[];
  painPoints?: string[];
  solutionTypes?: AtlasSolutionType[];
  whereUsed?: string[];
  whenNotUsed?: string[];
  questions?: string[];
  requiredInput?: string[];
  mediaPlan?: AtlasMediaPlan[];
  cta?: AtlasCta;
  directionRoute?: string;
  presentRoute?: string;
  ref?: string;
  subnodes?: AtlasSubnode[];
}

export interface AtlasManifesto {
  headline: string;
  subline: string;
  editorialSubline: string;
  productTitle: string;
  productPulse: string;
  pulseLead: string;
  centerTitle: string;
  centerTagline: string;
  exploreLabel: string;
}

export interface AtlasGraph {
  manifesto: AtlasManifesto;
  nodes: AtlasNodeContent[];
}
