import type { DirectionMeta, SlideContent } from "@/content/types";
import { HookSlide } from "./slides/HookSlide";
import { PainSlide } from "./slides/PainSlide";
import { BeforeAfterSlide } from "./slides/BeforeAfterSlide";
import { SolutionLogicSlide } from "./slides/SolutionLogicSlide";
import { CadViewerSlide } from "./slides/CadViewerSlide";
import { CtaSlide } from "./slides/CtaSlide";

export interface SlideRendererProps {
  slide: SlideContent;
  meta: DirectionMeta;
  slideIndex: number;
  slideCount: number;
}

export function SlideRenderer({
  slide,
  meta,
  slideIndex,
  slideCount,
}: SlideRendererProps) {
  const context = { meta, slideIndex, slideCount };

  switch (slide.type) {
    case "hook":
      return <HookSlide content={slide} {...context} />;
    case "pain":
      return <PainSlide content={slide} {...context} />;
    case "before-after":
      return <BeforeAfterSlide content={slide} {...context} />;
    case "solution-logic":
      return <SolutionLogicSlide content={slide} {...context} />;
    case "cad-viewer":
      return <CadViewerSlide content={slide} {...context} />;
    case "cta":
      return <CtaSlide content={slide} {...context} />;
    default:
      return null;
  }
}
