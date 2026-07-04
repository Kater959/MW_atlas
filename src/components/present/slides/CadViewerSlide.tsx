import type { CadViewerSlideContent } from "@/content/types";
import { MultilineText } from "../MultilineText";
import { SlideFrame, type SlideContextProps } from "../SlideFrame";
import { CadViewerSlot } from "@/components/cad/CadViewerSlot";

export function CadViewerSlide({
  content,
  ...ctx
}: SlideContextProps & { content: CadViewerSlideContent }) {
  return (
    <SlideFrame {...ctx}>
      <h2 className="max-w-4xl text-[length:var(--title-size)] leading-[1.08] font-medium tracking-[-0.02em] text-[var(--text-primary)]">
        <MultilineText text={content.title} />
      </h2>
      <p className="mt-4 max-w-3xl text-[length:var(--body-size)] leading-relaxed text-[var(--text-muted)]">
        <MultilineText text={content.subtitle} />
      </p>
      <div className="mt-8">
        <CadViewerSlot
          model={null}
          nodes={content.nodes}
          footer={content.viewerFooter}
        />
      </div>
      <p className="mt-8 max-w-3xl text-[length:var(--body-size)] leading-relaxed text-[var(--text-primary)]">
        <MultilineText text={content.slideFooter} />
      </p>
    </SlideFrame>
  );
}
