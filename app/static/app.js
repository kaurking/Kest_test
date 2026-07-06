const form = document.querySelector("#quote-form");
const input = document.querySelector("#registration-number");
const message = document.querySelector("#form-message");
const offersList = document.querySelector("#offers-list");
const resultsTitle = document.querySelector("#results-title");
const resultsMeta = document.querySelector("#results-meta");
const submitButton = form.querySelector("button");

function formatPeriod(period) {
  return period === "month" ? "kuu" : "aasta";
}

function formatMoney(amount, currency) {
  return new Intl.NumberFormat("et-EE", {
    style: "currency",
    currency,
    maximumFractionDigits: 0,
  }).format(amount);
}

function renderOffers(data) {
  const offers = data.offers || [];

  resultsTitle.textContent = `Pakkumised numbrile ${data.registrationNumber}`;
  resultsMeta.textContent = `${offers.length} pakkumist järjestatud odavaimast kallimani`;
  offersList.innerHTML = "";

  offers.forEach((offer, index) => {
    const row = document.createElement("article");
    row.className = "offer-row";
    row.innerHTML = `
      <div class="rank">${index + 1}</div>
      <div>
        <p class="insurer">${offer.insurer}</p>
        <p class="details">MTPL liikluskindlustus · ${formatMoney(offer.premium, offer.currency)} / ${formatPeriod(offer.period)}</p>
      </div>
      <div class="price">
        <strong>${formatMoney(offer.annualPremium, offer.currency)}</strong>
        <span>võrdlushind aastas</span>
      </div>
    `;
    offersList.append(row);
  });
}

function showEmptyState(text) {
  resultsTitle.textContent = "Pakkumised ilmuvad siia";
  resultsMeta.textContent = "";
  offersList.innerHTML = `<div class="empty-state">${text}</div>`;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const registrationNumber = input.value.trim();
  message.textContent = "";

  if (!registrationNumber) {
    message.textContent = "Sisesta numbrimärk.";
    input.focus();
    return;
  }

  submitButton.disabled = true;

  try {
    const response = await fetch(
      `/api/mtpl/offers?registration_number=${encodeURIComponent(registrationNumber)}`
    );

    if (response.status === 404) {
      message.textContent = "Sellist autot ei leitud.";
      showEmptyState("Selle numbrimärgi kohta pakkumisi ei leitud.");
      return;
    }

    if (!response.ok) {
      message.textContent = "Pakkumisi ei saanud hetkel laadida.";
      return;
    }

    const data = await response.json();
    renderOffers(data);
  } catch {
    message.textContent = "Ühendus backendiga ebaõnnestus.";
  } finally {
    submitButton.disabled = false;
  }
});
