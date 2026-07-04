"use client";

import { useCallback, useEffect } from "react";
import type { AtlasVisual } from "@/content/atlas-types";
import { GlbModelViewer } from "./GlbModelViewer";

export type FullscreenVisual =
  | { kind: "image"; src: string; title: string; label?: string }
  | { kind: "model"; visual: AtlasVisual };

export function VisualFullscreen({
  item,
  onClose,
}: {
  item: FullscreenVisual;
  onClose: () => void;
}) {
  const handleKeyDown = useCallback(
    (event: KeyboardEvent) => {
      if (event.key === "Escape") onClose();
    },
    [onClose],
  );

  useEffect(() => {
    document.body.style.overflow = "hidden";
    window.addEventListener("keydown", handleKeyDown);
    return () => {
      document.body.style.overflow = "";
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [handleKeyDown]);

  const title = item.kind === "image" ? item.title : item.visual.title;
  const label =
    item.kind === "image"
      ? item.label
      : (item.visual.label ?? "GLB · 3D MODEL");

  return (
    <div
      className="fixed inset-0 z-[100] flex flex-col bg-[#050505]/96 backdrop-blur-sm"
      role="dialog"
      aria-modal
      aria-label={title}
    >
      <header className="flex h-14 shrink-0 items-center justify-between border-b border-[rgba(242,240,234,0.10)] px-6">
        <div className="min-w-0">
          <p className="truncate font-mono text-[10px] tracking-[0.25em] text-[var(--accent-signal)] uppercase">
            {label}
          </p>
          <p className="truncate text-sm text-[var(--text-muted)]">{title}</p>
        </div>
        <button
          type="button"
          onClick={onClose}
          className="shrink-0 border border-[var(--border-subtle)] px-4 py-2 font-mono text-[10px] tracking-widest text-[var(--text-muted)] uppercase hover:border-[var(--accent-signal)] hover:text-[var(--accent-signal)]"
        >
          ESC · Закрыть
        </button>
      </header>

      <div
        className="relative min-h-0 flex-1 p-4 sm:p-8"
        onClick={onClose}
        role="presentation"
      >
        <span className="pointer-events-none absolute inset-4 border border-[rgba(242,240,234,0.10)] sm:inset-8">
          <span className="absolute top-0 left-0 h-4 w-4 border-t border-l border-[var(--accent-signal)]" />
          <span className="absolute top-0 right-0 h-4 w-4 border-t border-r border-[var(--accent-signal)]" />
          <span className="absolute bottom-0 left-0 h-4 w-4 border-b border-l border-[var(--accent-signal)]" />
          <span className="absolute right-0 bottom-0 h-4 w-4 border-r border-b border-[var(--accent-signal)]" />
        </span>

        <div
          className="pointer-events-none absolute inset-0 opacity-30"
          style={{
            backgroundImage:
              "linear-gradient(rgba(242,240,234,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(242,240,234,0.04) 1px, transparent 1px)",
            backgroundSize: "48px 48px",
          }}
          aria-hidden
        />

        <div
          className="relative flex h-full w-full items-center justify-center"
          onClick={(event) => event.stopPropagation()}
        >
          {item.kind === "image" ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={item.src}
              alt={item.title}
              className="max-h-[calc(100dvh-10rem)] max-w-full cursor-zoom-out object-contain drop-shadow-[0_32px_64px_rgba(0,0,0,0.8)]"
              onClick={onClose}
            />
          ) : (
            <div className="h-full w-full max-h-[calc(100dvh-10rem)] max-w-6xl">
              <GlbModelViewer
                src={item.visual.src}
                poster={item.visual.poster}
                alt={item.visual.title}
                className="h-full w-full"
              />
            </div>
          )}
        </div>
      </div>

      <footer className="shrink-0 border-t border-[rgba(242,240,234,0.10)] px-6 py-3 text-center font-mono text-[9px] tracking-[0.2em] text-[var(--text-dim)] uppercase">
        MW PULSE · ENGINEERING DIAGNOSTIC CANVAS
        {item.kind === "model" && (
          <span>
            {" "}
            · drag to rotate · scroll to zoom
          </span>
        )}
      </footer>
    </div>
  );
}

function ExpandHint() {
  return (
    <div className="pointer-events-none absolute inset-0 z-[2] flex items-end justify-center bg-gradient-to-t from-[#050505]/80 via-transparent to-transparent p-4 opacity-0 transition-opacity group-hover:opacity-100">
      <span className="font-mono text-[9px] tracking-[0.22em] text-[var(--accent-signal)] uppercase">
        Fullscreen · click
      </span>
    </div>
  );
}

export function ClickableVisualFrame({
  children,
  onExpand,
  label = "Open fullscreen",
}: {
  children: React.ReactNode;
  onExpand: () => void;
  label?: string;
}) {
  return (
    <button
      type="button"
      onClick={onExpand}
      aria-label={label}
      className="group relative flex w-full cursor-zoom-in items-center justify-center border-0 bg-transparent p-0"
    >
      {children}
      <ExpandHint />
    </button>
  );
}
