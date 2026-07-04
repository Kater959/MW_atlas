"use client";

import { useState } from "react";
import { motion, useReducedMotion } from "motion/react";
import type { SolutionLogicSlideContent } from "@/content/types";
import { MultilineText } from "../MultilineText";
import { SlideFrame, type SlideContextProps } from "../SlideFrame";

export function SolutionLogicSlide({
  content,
  ...ctx
}: SlideContextProps & { content: SolutionLogicSlideContent }) {
  const [activeId, setActiveId] = useState(content.nodes[0]?.id ?? "");
  const reducedMotion = useReducedMotion();
  const active =
    content.nodes.find((n) => n.id === activeId) ?? content.nodes[0];

  return (
    <SlideFrame {...ctx}>
      <h2 className="max-w-4xl text-[length:var(--title-size)] leading-[1.08] font-medium tracking-[-0.02em] text-[var(--text-primary)]">
        <MultilineText text={content.title} />
      </h2>
      <p className="mt-6 max-w-3xl text-[length:var(--body-size)] leading-relaxed text-[var(--text-muted)]">
        {content.subtitle}
      </p>

      <div className="mt-10 grid gap-6 lg:grid-cols-[1fr_280px]">
        <ul className="space-y-2">
          {content.nodes.map((node, index) => (
            <motion.li
              key={node.id}
              initial={reducedMotion ? false : { opacity: 0, x: -8 }}
              animate={{ opacity: 1, x: 0 }}
              transition={
                reducedMotion
                  ? { duration: 0 }
                  : { delay: index * 0.06, duration: 0.4 }
              }
            >
              <button
                type="button"
                onClick={() => setActiveId(node.id)}
                className={`w-full rounded-sm border px-5 py-4 text-left transition-colors ${
                  activeId === node.id
                    ? "border-[var(--accent-steel)] bg-[var(--bg-elevated)]"
                    : "border-[var(--border-subtle)] bg-[var(--bg-panel)] hover:border-[var(--border-edge)]"
                }`}
              >
                <span className="font-mono text-xs tracking-widest text-[var(--text-mono)] uppercase">
                  {node.title}
                </span>
                <span className="mt-1 block text-sm text-[var(--text-muted)]">
                  {node.description}
                </span>
              </button>
            </motion.li>
          ))}
        </ul>

        {active && (
          <aside className="hidden rounded-sm border border-[var(--border-subtle)] bg-[var(--bg-panel)] p-6 lg:block">
            <p className="font-mono text-[10px] tracking-widest text-[var(--accent-steel)] uppercase">
              {active.title}
            </p>
            <p className="mt-3 text-sm leading-relaxed text-[var(--text-muted)]">
              {active.description}
            </p>
          </aside>
        )}
      </div>

      <p className="mt-10 max-w-3xl border-t border-[var(--border-subtle)] pt-8 text-[length:var(--body-size)] leading-relaxed text-[var(--text-muted)]">
        <MultilineText text={content.footer} />
      </p>
    </SlideFrame>
  );
}
