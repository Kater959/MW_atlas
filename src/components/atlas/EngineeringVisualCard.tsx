"use client";

import Image from "next/image";
import { useState } from "react";
import type { AtlasVisual } from "@/content/atlas-types";
import { GlbModelViewer } from "./GlbModelViewer";
import {
  ClickableVisualFrame,
  VisualFullscreen,
  type FullscreenVisual,
} from "./VisualFullscreen";

const PULSE_FOOTER = "MW PULSE · ENGINEERING DIAGNOSTIC CANVAS";

function CornerBrackets() {
  return (
    <>
      <span
        className="pointer-events-none absolute top-0 left-0 z-10 h-3 w-3 border-t border-l border-[var(--accent-signal)]"
        aria-hidden
      />
      <span
        className="pointer-events-none absolute top-0 right-0 z-10 h-3 w-3 border-t border-r border-[var(--accent-signal)]"
        aria-hidden
      />
      <span
        className="pointer-events-none absolute bottom-0 left-0 z-10 h-3 w-3 border-b border-l border-[var(--accent-signal)]"
        aria-hidden
      />
      <span
        className="pointer-events-none absolute right-0 bottom-0 z-10 h-3 w-3 border-r border-b border-[var(--accent-signal)]"
        aria-hidden
      />
    </>
  );
}

function GridBackdrop() {
  return (
    <div
      className="pointer-events-none absolute inset-0 opacity-40"
      style={{
        backgroundImage:
          "linear-gradient(rgba(242,240,234,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(242,240,234,0.04) 1px, transparent 1px)",
        backgroundSize: "24px 24px",
      }}
      aria-hidden
    />
  );
}

function VisualFallback({ title }: { title: string }) {
  return (
    <div className="flex h-48 w-full items-center justify-center px-6">
      <p className="font-mono text-[10px] tracking-widest text-[var(--text-dim)] uppercase">
        {title}
      </p>
    </div>
  );
}

function RenderImage({
  src,
  alt,
  className = "max-h-72 w-full object-contain",
}: {
  src: string;
  alt: string;
  className?: string;
}) {
  const [failed, setFailed] = useState(false);

  if (failed) {
    return <VisualFallback title={alt} />;
  }

  return (
    <Image
      src={src}
      alt={alt}
      width={1200}
      height={900}
      className={`relative z-[1] drop-shadow-[0_24px_48px_rgba(0,0,0,0.65)] ${className}`}
      onError={() => setFailed(true)}
      unoptimized
    />
  );
}

function ModelPreview({
  visual,
  onExpand,
}: {
  visual: AtlasVisual;
  onExpand: () => void;
}) {
  const poster = visual.poster ?? visual.src;

  return (
    <div className="relative flex min-h-[280px] w-full items-center justify-center p-4">
      <GridBackdrop />
      <div className="relative z-[1] h-[260px] w-full">
        <GlbModelViewer
          src={visual.src}
          poster={poster}
          alt={visual.title}
          autoRotate={false}
          className="h-full w-full rounded-sm"
        />
      </div>
      <button
        type="button"
        onClick={onExpand}
        className="absolute top-5 right-5 z-10 border border-[var(--border-subtle)] bg-[#050505]/90 px-3 py-2 font-mono text-[9px] tracking-[0.2em] text-[var(--text-muted)] uppercase backdrop-blur-sm transition-colors hover:border-[var(--accent-signal)] hover:text-[var(--accent-signal)]"
      >
        Fullscreen
      </button>
      <p className="pointer-events-none absolute bottom-5 left-1/2 z-10 -translate-x-1/2 font-mono text-[9px] tracking-[0.2em] text-[var(--text-dim)] uppercase">
        GLB · drag to rotate
      </p>
    </div>
  );
}

export function EngineeringVisualCard({ visual }: { visual: AtlasVisual }) {
  const [fullscreen, setFullscreen] = useState<FullscreenVisual | null>(null);
  const isModel = visual.type === "model";
  const label = visual.label ?? visual.title.toUpperCase();
  const subtitle =
    visual.subtitle ?? (isModel ? "GLB · 3D MODEL" : "RENDER · CONCEPT VIEW");

  const openImageFullscreen = () => {
    setFullscreen({
      kind: "image",
      src: visual.src,
      title: visual.title,
      label: visual.label,
    });
  };

  const openModelFullscreen = () => {
    setFullscreen({ kind: "model", visual });
  };

  return (
    <>
      <figure className="engineering-visual-card relative overflow-hidden border border-[rgba(242,240,234,0.10)] bg-[#050505]">
        <CornerBrackets />

        <div className="engineering-visual-card__grid border-b border-[rgba(242,240,234,0.08)] px-5 py-4">
          <p className="font-mono text-[10px] tracking-[0.22em] text-[var(--accent-signal)] uppercase">
            {label}
          </p>
          <p className="mt-1 font-mono text-[9px] tracking-[0.18em] text-[var(--text-dim)] uppercase">
            {subtitle}
          </p>
        </div>

        {isModel ? (
          <ModelPreview visual={visual} onExpand={openModelFullscreen} />
        ) : (
          <ClickableVisualFrame
            onExpand={openImageFullscreen}
            label={`Открыть на весь экран: ${visual.title}`}
          >
            <div className="relative flex min-h-[220px] items-center justify-center p-6">
              <GridBackdrop />
              <RenderImage src={visual.src} alt={visual.title} />
            </div>
          </ClickableVisualFrame>
        )}

        {visual.callouts && visual.callouts.length > 0 && (
          <div className="border-t border-[rgba(242,240,234,0.08)] px-5 py-4">
            <p className="mb-3 font-mono text-[9px] tracking-[0.2em] text-[var(--text-dim)] uppercase">
              Callouts
            </p>
            <ul className="space-y-2">
              {visual.callouts.map((callout) => (
                <li
                  key={callout.label}
                  className="border-l border-[var(--accent-signal)] pl-3"
                >
                  <span className="font-mono text-[10px] tracking-widest text-[var(--accent-signal)] uppercase">
                    {callout.label}
                  </span>
                  {callout.description && (
                    <span className="mt-0.5 block text-xs text-[var(--text-muted)]">
                      {callout.description}
                    </span>
                  )}
                </li>
              ))}
            </ul>
          </div>
        )}

        <figcaption className="border-t border-[rgba(242,240,234,0.08)] px-5 py-3">
          {visual.caption && (
            <p className="text-sm leading-relaxed text-[var(--text-muted)]">
              {visual.caption}
            </p>
          )}
          <p className="mt-2 font-mono text-[8px] tracking-[0.2em] text-[var(--text-dim)] uppercase">
            {PULSE_FOOTER}
          </p>
        </figcaption>
      </figure>

      {fullscreen && (
        <VisualFullscreen
          item={fullscreen}
          onClose={() => setFullscreen(null)}
        />
      )}
    </>
  );
}
