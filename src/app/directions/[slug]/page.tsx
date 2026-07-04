import Link from "next/link";
import { notFound } from "next/navigation";
import { getDirectionDeck } from "@/content";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  const deck = getDirectionDeck(slug);
  if (!deck) return { title: "Metalwork Pulse" };

  return {
    title: `${deck.meta.ref} · ${deck.meta.titleRu} — Metalwork Pulse`,
  };
}

export default async function DirectionPage({ params }: PageProps) {
  const { slug } = await params;
  const deck = getDirectionDeck(slug);
  if (!deck) notFound();

  return (
    <main className="engineering-grid flex min-h-dvh flex-col items-center justify-center px-[var(--slide-padding-x)] py-[var(--slide-padding-y)]">
      <div className="relative z-10 max-w-lg text-center">
        <p className="font-mono text-[10px] tracking-widest text-[var(--text-mono)] uppercase">
          {deck.meta.ref} · {deck.meta.label}
        </p>
        <h1 className="mt-4 text-3xl font-medium text-[var(--text-primary)]">
          {deck.meta.titleRu}
        </h1>
        <p className="mt-4 text-[var(--text-muted)]">
          Подробная страница направления — в разработке.
          Сейчас доступны Metalwork Pulse canvas и Present Mode.
        </p>
        <div className="mt-10 flex flex-col gap-3 sm:flex-row sm:justify-center">
          <Link
            href="/atlas"
            className="inline-flex items-center justify-center rounded-sm border border-[var(--accent-steel)] px-6 py-3 font-mono text-[10px] tracking-widest text-[var(--text-primary)] uppercase"
          >
            Открыть Metalwork Pulse
          </Link>
          <Link
            href={`/present/${slug}`}
            className="inline-flex items-center justify-center rounded-sm border border-[var(--border-subtle)] px-6 py-3 font-mono text-[10px] tracking-widest text-[var(--text-muted)] uppercase"
          >
            Present Mode
          </Link>
        </div>
      </div>
    </main>
  );
}
