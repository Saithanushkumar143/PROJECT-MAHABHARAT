import React, { useState } from "react";
import { fetchWisdom } from "../services/api";

const Home = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!query) return;

    setLoading(true);
    setError("");
    
    try {
      const result = await fetchWisdom(query);
      setResponse(result);
    } catch (error) {
      setError("No wisdom found or API error.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-900 text-white">
      <h1 className="text-5xl font-bold mb-6">Mahabharata Wisdom</h1>

      <div className="w-full max-w-md">
        <input
          type="text"
          placeholder="Enter your problem..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full p-3 border rounded-lg text-black"
        />
        <button
          onClick={handleSearch}
          className="mt-4 w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
        >
          {loading ? "Loading..." : "Get Wisdom"}
        </button>
      </div>

      {error && <p className="text-red-500 mt-4">{error}</p>}

      {response && (
        <div className="mt-8 w-full max-w-2xl p-6 bg-gray-800 rounded-lg shadow-md">
          <h2 className="text-3xl font-bold">{response.scenario}</h2>
          <p className="mt-4"><strong>Characters:</strong> {response.characters}</p>
          <p className="mt-2"><strong>Lesson:</strong> {response.lesson}</p>
          <p className="mt-2"><strong>Shloka:</strong> {response.shloka}</p>
        </div>
      )}
    </div>
  );
};

export default Home;
