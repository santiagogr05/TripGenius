type DashboardData = {
  upcoming_trips: Array<{
    id: string;
    destination: string;
    start_date: string;
    end_date: string;
    travelers: number;
    status: string;
  }>;
  favorite_places: Array<{
    id: string;
    name: string;
    country: string;
  }>;
};

async function getDashboard(): Promise<DashboardData> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
  const res = await fetch(`${baseUrl}/api/dashboard`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load dashboard");
  return res.json();
}

export default async function DashboardPage() {
  const data = await getDashboard();

  return (
    <div className="min-h-screen bg-zinc-50 p-8">
      <div className="mx-auto max-w-5xl space-y-8">
        <header className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-semibold text-zinc-900">My Trips</h1>
            <p className="text-zinc-600">Overview of your travel information</p>
          </div>
          <button className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
            + Create New Trip
          </button>
        </header>

        <section className="space-y-3">
          <h2 className="text-xl font-semibold text-zinc-900">Upcoming Trips</h2>
          <div className="grid gap-4 md:grid-cols-2">
            {data.upcoming_trips.map((t) => (
              <a
                key={t.id}
                href={`/trips/${t.id}`}
                className="rounded-xl border bg-white p-5 shadow-sm hover:shadow-md"
              >
                <div className="flex items-start justify-between">
                  <div>
                    <p className="text-lg font-semibold text-zinc-900">{t.destination}</p>
                    <p className="text-sm text-zinc-500">
                      {t.start_date} → {t.end_date}
                    </p>
                  </div>
                  <span className="rounded-full bg-zinc-100 px-3 py-1 text-xs text-zinc-700">
                    {t.status}
                  </span>
                </div>
                <div className="mt-4 text-sm text-zinc-700">
                  Travelers: <strong>{t.travelers}</strong>
                </div>
                <div className="mt-4">
                  <div className="w-full rounded-lg bg-blue-50 px-4 py-2 text-center text-blue-700 hover:bg-blue-100">
                    View details
                  </div>
                </div>
              </a>
            ))}
          </div>
        </section>

        <section className="space-y-3">
          <h2 className="text-xl font-semibold text-zinc-900">Favorite Places</h2>
          <div className="grid gap-4 sm:grid-cols-2 md:grid-cols-4">
            {data.favorite_places.map((p) => (
              <div key={p.id} className="rounded-xl border bg-white p-4 shadow-sm">
                <div className="text-base font-semibold text-zinc-900">{p.name}</div>
                <div className="text-sm text-zinc-500">{p.country}</div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}