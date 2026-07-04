import { notFound } from "next/navigation";
import { Suspense } from "react";
import { getDirectionDeck } from "@/content";
import { DirectionDeckView } from "@/components/present/DirectionDeck";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  const deck = getDirectionDeck(slug);
  if (!deck) return { title: "Metalwork Pulse — Present" };

  return {
    title: `Present · ${deck.meta.ref} — Metalwork Pulse`,
    description: deck.meta.titleRu,
  };
}

export default async function PresentPage({ params }: PageProps) {
  const { slug } = await params;
  const deck = getDirectionDeck(slug);
  if (!deck) notFound();

  return (
    <Suspense fallback={<DeckLoading />}>
      <DirectionDeckView
        deck={deck}
        basePath={`/present/${slug}`}
      />
    </Suspense>
  );
}

function DeckLoading() {
  return (
    <div className="flex h-dvh items-center justify-center bg-[var(--bg-deck)]">
      <p className="font-mono text-xs tracking-widest text-[var(--text-muted)] uppercase">
        Loading present…
      </p>
    </div>
  );
}
