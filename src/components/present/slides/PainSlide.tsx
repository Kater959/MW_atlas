"use client";

import { motion, useReducedMotion } from "motion/react";
import type { PainSlideContent } from "@/content/types";
import { MultilineText } from "../MultilineText";
import { SlideFrame, type SlideContextProps } from "../SlideFrame";

export function PainSlide({
  content,
  ...ctx
}: SlideContextProps & { content: PainSlideContent }) {
  const reducedMotion = useReducedMotion();

  return (
    <SlideFrame {...ctx}>
      <h2 className="max-w-5xl text-[length:var(--title-size)] leading-[1.08] font-medium tracking-[-0.02em] text-[var(--text-primary)]">
        <MultilineText text={content.title} />
      </h2>
      <p className="mt-8 max-w-3xl text-[length:var(--body-size)] leading-relaxed text-[var(--accent-signal)]">
        <MultilineText text={content.subtitle} />
      </p>
      <ul className="mt-10 flex flex-wrap gap-3">
        {content.bullets.map((bullet, index) => (
          <motion.li
            key={bullet}
            initial={reducedMotion ? false : { opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={
              reducedMotion
                ? { duration: 0 }
                : { delay: index * 0.08, duration: 0.45, ease: [0.16, 1, 0.3, 1] }
            }
            className="rounded-sm border border-[var(--border-subtle)] bg-[var(--bg-elevated)] px-5 py-3 font-mono text-sm tracking-wide text-[var(--text-mono)]"
          >
            {bullet}
          </motion.li>
        ))}
      </ul>
    </SlideFrame>
  );
}
