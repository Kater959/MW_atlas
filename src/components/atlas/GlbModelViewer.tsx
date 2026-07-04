"use client";

import { useEffect } from "react";

export interface GlbModelViewerProps {
  src: string;
  poster?: string;
  alt?: string;
  className?: string;
  autoRotate?: boolean;
}

export function GlbModelViewer({
  src,
  poster,
  alt = "3D model",
  className = "h-full w-full",
  autoRotate = true,
}: GlbModelViewerProps) {
  useEffect(() => {
    void import("@google/model-viewer");
  }, []);

  return (
    <model-viewer
      src={src}
      poster={poster}
      alt={alt}
      camera-controls
      touch-action="pan-y"
      auto-rotate={autoRotate}
      exposure="1.1"
      shadow-intensity="0.6"
      className={className}
      style={{
        width: "100%",
        height: "100%",
        background: "#050505",
      } as React.CSSProperties}
    />
  );
}
