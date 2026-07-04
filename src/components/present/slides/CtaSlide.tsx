import type { CtaSlideContent } from "@/content/types";
import { MultilineText } from "../MultilineText";
import { SlideFrame, type SlideContextProps } from "../SlideFrame";

export function CtaSlide({
  content,
  ...ctx
}: SlideContextProps & { content: CtaSlideContent }) {
  return (
    <SlideFrame {...ctx}>
      <h2 className="max-w-4xl text-[length:var(--title-size)] leading-[1.08] font-medium tracking-[-0.02em] text-[var(--text-primary)]">
        <MultilineText text={content.title} />
      </h2>
      <ul className="mt-10 max-w-3xl space-y-3">
        {content.bullets.map((bullet) => (
          <li
            key={bullet}
            className="flex gap-4 text-[length:var(--body-size)] leading-relaxed text-[var(--text-muted)]"
          >
            <span
              className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-[var(--accent-steel)]"
              aria-hidden
            />
            {bullet}
          </li>
        ))}
      </ul>
      <div className="mt-12">
        <a
          href={content.primary.href}
          className="inline-flex items-center justify-center rounded-sm border border-[var(--accent-signal)] bg-[var(--accent-signal)]/10 px-8 py-4 font-mono text-xs tracking-widest text-[var(--accent-signal)] uppercase transition-colors hover:bg-[var(--accent-signal)]/20"
        >
          {content.primary.label}
        </a>
      </div>
      <p className="mt-10 max-w-2xl text-[length:var(--body-size)] leading-relaxed text-[var(--text-primary)]">
        <MultilineText text={content.secondaryText} />
      </p>
    </SlideFrame>
  );
}
