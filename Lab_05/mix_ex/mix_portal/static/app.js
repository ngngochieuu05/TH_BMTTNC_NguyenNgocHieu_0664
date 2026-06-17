const state = {
  ws: null,
  rsaCiphertext: "",
  rsaSignature: "",
  eccCiphertext: "",
  eccSignature: "",
};

function setOutput(id, value) {
  document.getElementById(id).textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

async function postJson(url, payload) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return response.json();
}

async function getJson(url) {
  const response = await fetch(url);
  return response.json();
}

async function sendSteg(url) {
  const file = document.getElementById("steg-file").files[0];
  if (!file) {
    setOutput("steg-output", "Hãy chọn ảnh trước");
    return;
  }
  const formData = new FormData();
  formData.append("image", file);
  formData.append("message", document.getElementById("steg-message").value);
  const response = await fetch(url, { method: "POST", body: formData });
  return response;
}

document.addEventListener("click", async (event) => {
  const action = event.target.dataset.action;
  if (!action) return;

  try {
    if (action === "overview") {
      setOutput("overview-output", await getJson("/api/overview"));
    }
    if (action === "ws-connect") {
      if (state.ws) state.ws.close();
      const protocol = location.protocol === "https:" ? "wss:" : "ws:";
      state.ws = new WebSocket(`${protocol}//${location.host}/ws/random-words`);
      state.ws.onmessage = (message) => {
        const current = document.getElementById("ws-output").textContent;
        setOutput("ws-output", `${current}${message.data}\n`);
      };
    }
    if (action === "ws-disconnect" && state.ws) {
      state.ws.close();
      state.ws = null;
    }
    if (action === "basic-greet") {
      setOutput("basic-output", await postJson("/api/basics/greet", {
        name: document.getElementById("basic-name").value,
        age: Number(document.getElementById("basic-age").value),
      }));
    }
    if (action === "basic-circle") {
      setOutput("basic-output", await postJson("/api/basics/circle-area", {
        radius: Number(document.getElementById("basic-radius").value),
      }));
    }
    if (action === "basic-parity") {
      setOutput("basic-output", await postJson("/api/basics/parity", {
        number: Number(document.getElementById("basic-number").value),
      }));
    }
    if (action === "basic-even-sum") {
      setOutput("basic-output", await postJson("/api/basics/even-sum", {
        values: document.getElementById("basic-values").value.split(",").map((item) => Number(item.trim())),
      }));
    }
    if (action === "basic-reverse") {
      setOutput("basic-output", await postJson("/api/basics/reverse", {
        text: document.getElementById("basic-text").value,
      }));
    }
    if (action === "student-add") {
      setOutput("student-output", await postJson("/api/students", {
        name: document.getElementById("student-name").value,
        sex: document.getElementById("student-sex").value,
        major: document.getElementById("student-major").value,
        diem_tb: Number(document.getElementById("student-diem").value),
      }));
    }
    if (action === "student-list") setOutput("student-output", await getJson("/api/students"));
    if (action === "student-search") {
      const keyword = encodeURIComponent(document.getElementById("student-search").value);
      setOutput("student-output", await getJson(`/api/students/search?q=${keyword}`));
    }
    if (action === "student-sort-name") setOutput("student-output", await getJson("/api/students/sort/name"));
    if (action === "student-sort-score") setOutput("student-output", await getJson("/api/students/sort/score"));
    if (action === "classical-run") {
      setOutput("classical-output", await postJson("/api/classical", {
        algorithm: document.getElementById("classical-algorithm").value,
        action: document.getElementById("classical-action").value,
        text: document.getElementById("classical-text").value,
        key: document.getElementById("classical-key").value,
      }));
    }
    if (action === "hash-run") {
      setOutput("hash-output", await postJson("/api/hash", {
        algorithm: document.getElementById("hash-algorithm").value,
        text: document.getElementById("hash-text").value,
      }));
    }
    if (action === "base64-encode") {
      setOutput("hash-output", await postJson("/api/base64/encode", {
        text: document.getElementById("base64-text").value,
      }));
    }
    if (action === "base64-decode") {
      setOutput("hash-output", await postJson("/api/base64/decode", {
        text: document.getElementById("base64-text").value,
      }));
    }
    if (action === "rsa-generate") setOutput("modern-output", await postJson("/api/rsa/generate", {}));
    if (action === "rsa-encrypt") {
      const data = await postJson("/api/rsa/encrypt", { message: document.getElementById("modern-text").value });
      state.rsaCiphertext = data.result;
      setOutput("modern-output", data);
    }
    if (action === "rsa-decrypt") {
      setOutput("modern-output", await postJson("/api/rsa/decrypt", { ciphertext: state.rsaCiphertext }));
    }
    if (action === "rsa-sign") {
      const data = await postJson("/api/rsa/sign", { message: document.getElementById("modern-text").value });
      state.rsaSignature = data.result;
      setOutput("modern-output", data);
    }
    if (action === "rsa-verify") {
      setOutput("modern-output", await postJson("/api/rsa/verify", {
        message: document.getElementById("modern-text").value,
        signature: state.rsaSignature,
      }));
    }
    if (action === "ecc-generate") setOutput("modern-output", await postJson("/api/ecc/generate", {}));
    if (action === "ecc-encrypt") {
      const data = await postJson("/api/ecc/encrypt", { message: document.getElementById("modern-text").value });
      state.eccCiphertext = data.result;
      setOutput("modern-output", data);
    }
    if (action === "ecc-decrypt") {
      setOutput("modern-output", await postJson("/api/ecc/decrypt", { ciphertext: state.eccCiphertext }));
    }
    if (action === "ecc-sign") {
      const data = await postJson("/api/ecc/sign", { message: document.getElementById("modern-text").value });
      state.eccSignature = data.result;
      setOutput("modern-output", data);
    }
    if (action === "ecc-verify") {
      setOutput("modern-output", await postJson("/api/ecc/verify", {
        message: document.getElementById("modern-text").value,
        signature: state.eccSignature,
      }));
    }
    if (action === "blockchain-add") {
      setOutput("blockchain-output", await postJson("/api/blockchain/transactions", {
        sender: document.getElementById("tx-sender").value,
        receiver: document.getElementById("tx-receiver").value,
        amount: Number(document.getElementById("tx-amount").value),
      }));
    }
    if (action === "blockchain-mine") setOutput("blockchain-output", await postJson("/api/blockchain/mine", {}));
    if (action === "blockchain-state") setOutput("blockchain-output", await getJson("/api/blockchain"));
    if (action === "steg-encode") {
      const response = await sendSteg("/api/steganography/encode");
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = "encoded_image.png";
      anchor.click();
      setOutput("steg-output", "Ảnh đã được mã hóa và tải xuống");
    }
    if (action === "steg-decode") {
      const response = await sendSteg("/api/steganography/decode");
      setOutput("steg-output", await response.json());
    }
    if (action === "scripts-load") setOutput("scripts-output", await getJson("/api/scripts"));
  } catch (error) {
    const target = action.startsWith("student")
      ? "student-output"
      : action.startsWith("basic")
        ? "basic-output"
        : action.startsWith("classical")
          ? "classical-output"
          : action.startsWith("hash") || action.startsWith("base64")
            ? "hash-output"
            : action.startsWith("rsa") || action.startsWith("ecc")
              ? "modern-output"
              : action.startsWith("blockchain")
                ? "blockchain-output"
                : action.startsWith("steg")
                  ? "steg-output"
                  : action.startsWith("ws")
                    ? "ws-output"
                    : "overview-output";
    setOutput(target, `Lỗi: ${error.message}`);
  }
});
