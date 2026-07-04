"use client";

import { motion, useReducedMotion } from "motion/react";
import type { BeforeAfterSlideContent } from "@/content/types";
import { MultilineText } from "../MultilineText";
import { SlideFrame, type SlideContextProps } from "../SlideFrame";
import { SchematicPanel } from "./SchematicPanel";

export function BeforeAfterSlide({
  content,
  ...ctx
}: SlideContextProps & { content: BeforeAfterSlideContent }) {
  const reducedMotion = useReducedMotion();

  return (
    <SlideFrame {...ctx}>
      <div className="grid gap-10 lg:grid-cols-2 lg:gap-12">
        <motion.div
          initial={reducedMotion ? false : { opacity: 0, x: -12 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: reducedMotion ? 0 : 0.5 }}
        >
          <h2 className="text-xl font-medium leading-snug text-[var(--text-muted)] sm:text-2xl">
            <MultilineText text={content.title} />
          </h2>
          <SchematicPanel variant="before" className="mt-6" />
          <ul className="mt-6 space-y-2">
            {content.before.map((item) => (
              <li
                key={item}
                className="flex gap-3 font-mono text-sm text-[var(--text-muted)]"
              >
                <span className="text-[var(--text-muted)]">—</span>
                {item}
              </li>
            ))}
          </ul>
        </motion.div>

        <motion.div
          initial={reducedMotion ? false : { opacity: 0, x: 12 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: reducedMotion ? 0 : 0.5, delay: reducedMotion ? 0 : 0.08 }}
        >
          <h2 className="text-xl font-medium leading-snug text-[var(--text-primary)] sm:text-2xl">
            <MultilineText text={content.afterTitle} />
          </h2>
          <SchematicPanel variant="after" className="mt-6" />
          <ul className="mt-6 space-y-2">
            {content.after.map((item) => (
              <li
                key={item}
                className="flex gap-3 font-mono text-sm text-[var(--text-primary)]"
              >
                <span className="text-[var(--accent-steel)]">+</span>
                {item}
              </li>
            ))}
          </ul>
        </motion.div>
      </div>
    </SlideFrame>
  );
}
