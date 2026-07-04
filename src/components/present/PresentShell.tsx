"use client";

import {
  useCallback,
  useEffect,
  useRef,
  useState,
  type ReactNode,
} from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { AnimatePresence, motion } from "motion/react";
import type { DirectionMeta } from "@/content/types";

export interface PresentShellProps {
  meta: DirectionMeta;
  slideCount: number;
  basePath: string;
  children: (props: { activeIndex: number }) => ReactNode;
}

const SWIPE_THRESHOLD = 50;

function useReducedMotion(): boolean {
  const [reduced, setReduced] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReduced(mq.matches);
    const handler = () => setReduced(mq.matches);
    mq.addEventListener("change", handler);
    return () => mq.removeEventListener("change", handler);
  }, []);

  return reduced;
}

export function PresentShell({
  meta,
  slideCount,
  basePath,
  children,
}: PresentShellProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const touchStartY = useRef<number | null>(null);
  const [activeIndex, setActiveIndex] = useState(0);
  const reducedMotion = useReducedMotion();

  const clampIndex = useCallback(
    (index: number) => Math.max(0, Math.min(slideCount - 1, index)),
    [slideCount],
  );

  const goTo = useCallback(
    (index: number) => {
      const next = clampIndex(index);
      setActiveIndex(next);
      router.replace(`${basePath}?slide=${next + 1}`, { scroll: false });
    },
    [basePath, clampIndex, router],
  );

  useEffect(() => {
    const slideParam = searchParams.get("slide");
    if (slideParam) {
      const parsed = parseInt(slideParam, 10);
      if (!Number.isNaN(parsed) && parsed >= 1 && parsed <= slideCount) {
        setActiveIndex(parsed - 1);
      }
    }
  }, [searchParams, slideCount]);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        router.push("/");
        return;
      }
      if (
        event.key === "ArrowDown" ||
        event.key === "ArrowRight" ||
        event.key === "PageDown" ||
        event.key === " "
      ) {
        event.preventDefault();
        goTo(activeIndex + 1);
      }
      if (
        event.key === "ArrowUp" ||
        event.key === "ArrowLeft" ||
        event.key === "PageUp"
      ) {
        event.preventDefault();
        goTo(activeIndex - 1);
      }
      if (event.key === "Home") {
        event.preventDefault();
        goTo(0);
      }
      if (event.key === "End") {
        event.preventDefault();
        goTo(slideCount - 1);
      }
    };

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [activeIndex, goTo, router, slideCount]);

  const onTouchStart = (event: React.TouchEvent) => {
    touchStartY.current = event.touches[0]?.clientY ?? null;
  };

  const onTouchEnd = (event: React.TouchEvent) => {
    if (touchStartY.current === null) return;
    const deltaY =
      touchStartY.current - (event.changedTouches[0]?.clientY ?? 0);
    if (Math.abs(deltaY) > SWIPE_THRESHOLD) {
      goTo(activeIndex + (deltaY > 0 ? 1 : -1));
    }
    touchStartY.current = null;
  };

  const transition = reducedMotion
    ? { duration: 0 }
    : { duration: 0.55, ease: [0.16, 1, 0.3, 1] as const };

  return (
    <div
      className="relative flex h-dvh flex-col overflow-hidden bg-[var(--bg-deck)]"
      onTouchStart={onTouchStart}
      onTouchEnd={onTouchEnd}
    >
      <header className="z-20 flex h-10 shrink-0 items-center justify-between border-b border-[var(--border-subtle)] bg-[var(--bg-deck)]/90 px-[var(--slide-padding-x)] backdrop-blur-sm">
        <div className="flex min-w-0 items-baseline gap-3">
          <span className="font-mono text-[10px] tracking-[0.2em] text-[var(--text-mono)] uppercase">
            Metalwork Pulse
          </span>
          <span className="hidden truncate font-mono text-[10px] tracking-[0.15em] text-[var(--text-muted)] uppercase sm:inline">
            {meta.ref} · {meta.label}
          </span>
        </div>
        <div className="flex items-center gap-4">
          <span className="hidden font-mono text-[9px] tracking-widest text-[var(--text-muted)] sm:inline">
            ESC
          </span>
          <span className="font-mono text-[10px] tracking-widest text-[var(--text-muted)] tabular-nums">
            {String(activeIndex + 1).padStart(2, "0")} /{" "}
            {String(slideCount).padStart(2, "0")}
          </span>
        </div>
      </header>

      <main className="relative min-h-0 flex-1">
        <AnimatePresence mode="wait">
          <motion.div
            key={activeIndex}
            initial={reducedMotion ? false : { opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={reducedMotion ? undefined : { opacity: 0, y: -8 }}
            transition={transition}
            className="absolute inset-0"
          >
            {children({ activeIndex })}
          </motion.div>
        </AnimatePresence>
      </main>

      <nav
        className="z-20 flex h-12 shrink-0 items-center justify-center gap-2 border-t border-[var(--border-subtle)] bg-[var(--bg-deck)]/90 backdrop-blur-sm"
        aria-label="Навигация по слайдам"
      >
        {Array.from({ length: slideCount }, (_, index) => (
          <button
            key={index}
            type="button"
            onClick={() => goTo(index)}
            aria-label={`Слайд ${index + 1}`}
            aria-current={index === activeIndex ? "step" : undefined}
            className={`h-2 rounded-full transition-all duration-300 ${
              index === activeIndex
                ? "w-6 bg-[var(--accent-steel)]"
                : "w-2 bg-[var(--border-edge)] hover:bg-[var(--text-muted)]"
            }`}
          />
        ))}
      </nav>
    </div>
  );
}
