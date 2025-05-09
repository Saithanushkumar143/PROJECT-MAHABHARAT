import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000";  // Backend Flask server

export const fetchWisdom = async (query) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/get_wisdom?query=${query}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching wisdom:", error);
    throw error;
  }
};
