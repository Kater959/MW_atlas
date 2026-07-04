import type { HookSlideContent } from "@/content/types";
import { MultilineText } from "../MultilineText";
import { SlideFrame, type SlideContextProps } from "../SlideFrame";

export function HookSlide({
  content,
  ...ctx
}: SlideContextProps & { content: HookSlideContent }) {
  return (
    <SlideFrame {...ctx}>
      <p className="mb-6 font-mono text-[length:var(--label-size)] tracking-[0.25em] text-[var(--text-mono)] uppercase">
        {ctx.meta.ref} · {ctx.meta.label}
      </p>
      <h1 className="max-w-5xl text-[length:var(--title-size)] leading-[1.08] font-medium tracking-[-0.02em] text-[var(--text-primary)]">
        <MultilineText text={content.title} />
      </h1>
      <p className="mt-8 max-w-3xl text-[length:var(--body-size)] leading-relaxed text-[var(--text-muted)]">
        <MultilineText text={content.subtitle} />
      </p>
      <ul className="mt-10 max-w-3xl space-y-4 border-t border-[var(--border-subtle)] pt-8">
        {content.bullets.map((bullet) => (
          <li
            key={bullet}
            className="flex gap-4 text-[length:var(--body-size)] leading-relaxed text-[var(--text-primary)]"
          >
            <span
              className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-[var(--accent-steel)]"
              aria-hidden
            />
            {bullet}
          </li>
        ))}
      </ul>
    </SlideFrame>
  );
}
