function MultilineText({
  text,
  className,
}: {
  text: string;
  className?: string;
}) {
  return (
    <>
      {text.split("\n").map((line, i, arr) => (
        <span key={i} className={className}>
          {line}
          {i < arr.length - 1 && <br />}
        </span>
      ))}
    </>
  );
}

export { MultilineText };
