import type { DirectionMeta } from "@/content/types";

export interface SlideFrameProps {
  meta: DirectionMeta;
  slideIndex: number;
  slideCount: number;
  children: React.ReactNode;
  className?: string;
}

export function SlideFrame({
  meta,
  slideIndex,
  slideCount,
  children,
  className = "",
}: SlideFrameProps) {
  return (
    <section
      className={`engineering-grid relative flex h-full flex-col justify-center px-[var(--slide-padding-x)] py-[var(--slide-padding-y)] ${className}`}
      aria-label={`Слайд ${slideIndex + 1} из ${slideCount}`}
    >
      <div
        className="pointer-events-none absolute inset-0 opacity-[0.35]"
        style={{
          background:
            "radial-gradient(ellipse 80% 60% at 50% 50%, transparent 0%, var(--bg-deck) 75%)",
        }}
      />
      <div className="relative z-10 mx-auto w-full max-w-6xl">{children}</div>
      <footer className="absolute right-[var(--slide-padding-x)] bottom-6 left-[var(--slide-padding-x)] z-10 flex items-end justify-between gap-4">
        <p className="font-mono text-[10px] tracking-[0.15em] text-[var(--text-muted)] uppercase">
          {meta.ref} · {meta.label}
        </p>
        <p className="hidden font-mono text-[10px] tracking-widest text-[var(--text-muted)] sm:block">
          {meta.titleRu}
        </p>
      </footer>
    </section>
  );
}

export interface SlideContextProps {
  meta: DirectionMeta;
  slideIndex: number;
  slideCount: number;
}
