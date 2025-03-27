interface EmptyProps {
  resourceName: string;
}

function Empty({ resourceName }: EmptyProps) {
  return (
    <div>
      <p>Неможливо знайти {resourceName}</p>
    </div>
  );
}

export default Empty;
