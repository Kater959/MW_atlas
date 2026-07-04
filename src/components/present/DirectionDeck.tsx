"use client";

import type { DirectionDeck } from "@/content/types";
import { PresentShell } from "./PresentShell";
import { SlideRenderer } from "./SlideRenderer";

export interface DirectionDeckProps {
  deck: DirectionDeck;
  basePath: string;
}

export function DirectionDeckView({ deck, basePath }: DirectionDeckProps) {
  return (
    <PresentShell
      meta={deck.meta}
      slideCount={deck.slides.length}
      basePath={basePath}
    >
      {({ activeIndex }) => (
        <SlideRenderer
          slide={deck.slides[activeIndex]!}
          meta={deck.meta}
          slideIndex={activeIndex}
          slideCount={deck.slides.length}
        />
      )}
    </PresentShell>
  );
}
