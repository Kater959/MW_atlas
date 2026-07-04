import type { DetailedHTMLProps, HTMLAttributes } from "react";

type ModelViewerAttributes = HTMLAttributes<HTMLElement> & {
  src?: string;
  poster?: string;
  alt?: string;
  "camera-controls"?: boolean;
  "auto-rotate"?: boolean;
  "touch-action"?: string;
  exposure?: string;
  "shadow-intensity"?: string;
  "environment-image"?: string;
};

declare module "react" {
  namespace JSX {
    interface IntrinsicElements {
      "model-viewer": DetailedHTMLProps<ModelViewerAttributes, HTMLElement>;
    }
  }
}

export {};
