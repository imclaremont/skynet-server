document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const delivery_id = urlParams.get("delivery_id") || "";
  const apiUrl = `/api/delivery_info?delivery_id=${delivery_id}`;

  fetch(apiUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch delivery info");
      }
      return response.json();
    })
    .then((data) => {
      if (data) {
        document.querySelector(".delivery-id-card").textContent = `운송 번호: ${
          data.delivery_id || "00000000"
        }`;
        document.querySelector(
          "body > div > div.card > p:nth-child(2)"
        ).textContent =
          "출발지: " + String(data.edge_origin_name || "정보 없음");
        document.querySelector(
          "body > div > div.card > p:nth-child(3)"
        ).textContent =
          "다음 목적지: " + String(data.edge_destination_name || "정보 없음");
        document.querySelector(
          "body > div > div:nth-child(3) > p"
        ).textContent = data.content || "정보 없음";
        document.querySelector(
          "body > div > div:nth-child(4) > p"
        ).textContent = data.destination || "정보 없음";
        document.querySelector(
          "body > div > div:nth-child(5) > p"
        ).textContent = `${String(data.edt)}분` || "정보 없음";
      } else {
        console.error("Delivery data is empty or not found");
      }
    })
    .catch((error) => {
      console.error("Error fetching delivery info:", error);
    });
});
