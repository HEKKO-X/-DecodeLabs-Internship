import { useState } from "react";

function caesarShift(text, shift) {
  return text.split("").map(char => {
    if (/[a-zA-Z]/.test(char)) {
      const base = char >= "a" ? 97 : 65;
      return String.fromCharCode(((char.charCodeAt(0) - base + shift % 26 + 26) % 26) + base);
    }
    return char;
  }).join("");
}

function getBruteForce(text) {
  return Array.from({ length: 25 }, (_, i) => ({
    key: i + 1,
    result: caesarShift(text, -(i + 1))
  }));
}

export default function App() {
  const [tab, setTab]         = useState("encrypt");
  const [input, setInput]     = useState("");
  const [shift, setShift]     = useState(3);
  const [showBrute, setShowBrute] = useState(false);

  const encrypted = caesarShift(input, shift);
  const decrypted = caesarShift(input, -shift);
  const output    = tab === "encrypt" ? encrypted : decrypted;
  const bruteRows = getBruteForce(input);

  const pill = (active) => ({
    padding: "8px 24px",
    borderRadius: "999px",
    border: "none",
    cursor: "pointer",
    fontFamily: "monospace",
    fontSize: "13px",
    fontWeight: 500,
    background: active ? "#534AB7" : "transparent",
    color: active ? "#fff" : "#AFA9EC",
    transition: "all 0.2s",
  });

  const card = {
    background: "#0F1F3D",
    borderRadius: "10px",
    padding: "1rem 1.2rem",
    marginBottom: "1rem",
  };

  return (
    <div style={{ minHeight: "100vh", background: "#0A2540", fontFamily: "monospace", padding: "1.5rem", color: "#fff" }}>

      {/* Header */}
      <div style={{ textAlign: "center", marginBottom: "1.5rem" }}>
        <div style={{ fontSize: "2rem", marginBottom: "0.3rem" }}>🔐</div>
        <h1 style={{ margin: 0, fontSize: "1.3rem", color: "#fff" }}>Caesar Cipher Tool</h1>
        <p style={{ margin: "0.2rem 0 0", fontSize: "0.75rem", color: "#AFA9EC" }}>DecodeLabs · Cyber Security · Project 2</p>
      </div>

      {/* Tabs */}
      <div style={{ display: "flex", justifyContent: "center", gap: "8px", background: "#060F1E", borderRadius: "999px", padding: "4px", marginBottom: "1.5rem", width: "fit-content", margin: "0 auto 1.5rem" }}>
        {["encrypt", "decrypt", "brute"].map(t => (
          <button key={t} onClick={() => { setTab(t); setShowBrute(t === "brute"); }}
            style={pill(tab === t)}>
            {t === "brute" ? "Brute Force" : t.charAt(0).toUpperCase() + t.slice(1)}
          </button>
        ))}
      </div>

      {/* Input */}
      <div style={card}>
        <label style={{ fontSize: "11px", color: "#AFA9EC", letterSpacing: "2px", display: "block", marginBottom: "8px" }}>
          {tab === "brute" ? "ENTER CIPHERTEXT" : tab === "encrypt" ? "PLAINTEXT" : "CIPHERTEXT"}
        </label>
        <textarea
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder={tab === "encrypt" ? "Type your message here..." : "Paste ciphertext here..."}
          rows={3}
          style={{ width: "100%", boxSizing: "border-box", background: "#060F1E", border: "1px solid #1D2A4A", borderRadius: "8px", color: "#fff", fontFamily: "monospace", fontSize: "14px", padding: "0.7rem", resize: "vertical", outline: "none" }}
        />
      </div>

      {/* Shift slider — not shown on brute force */}
      {tab !== "brute" && (
        <div style={card}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "10px" }}>
            <label style={{ fontSize: "11px", color: "#AFA9EC", letterSpacing: "2px" }}>SHIFT KEY</label>
            <span style={{ fontSize: "20px", fontWeight: 700, color: "#534AB7", minWidth: "28px", textAlign: "right" }}>{shift}</span>
          </div>
          <input type="range" min="1" max="25" value={shift} onChange={e => setShift(Number(e.target.value))}
            style={{ width: "100%", accentColor: "#534AB7" }} />
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: "10px", color: "#3A5070", marginTop: "4px" }}>
            <span>1</span><span>25</span>
          </div>
        </div>
      )}

      {/* Output — encrypt / decrypt */}
      {tab !== "brute" && (
        <div style={{ ...card, borderLeft: "4px solid #1D9E75" }}>
          <label style={{ fontSize: "11px", color: "#9FE1CB", letterSpacing: "2px", display: "block", marginBottom: "8px" }}>
            {tab === "encrypt" ? "ENCRYPTED OUTPUT" : "DECRYPTED OUTPUT"}
          </label>
          <div style={{ background: "#060F1E", borderRadius: "8px", padding: "0.8rem 1rem", minHeight: "52px", fontSize: "14px", color: input ? "#1D9E75" : "#3A5070", wordBreak: "break-all", letterSpacing: "1px" }}>
            {input ? output : "Output will appear here..."}
          </div>
          {input && (
            <button onClick={() => navigator.clipboard?.writeText(output)}
              style={{ marginTop: "8px", background: "none", border: "1px solid #1D9E75", borderRadius: "6px", color: "#9FE1CB", fontSize: "11px", padding: "4px 12px", cursor: "pointer", fontFamily: "monospace" }}>
              Copy
            </button>
          )}
        </div>
      )}

      {/* Alphabet shift preview */}
      {tab !== "brute" && (
        <div style={card}>
          <label style={{ fontSize: "11px", color: "#AFA9EC", letterSpacing: "2px", display: "block", marginBottom: "10px" }}>ALPHABET SHIFT PREVIEW</label>
          <div style={{ overflowX: "auto" }}>
            <div style={{ display: "flex", gap: "4px", marginBottom: "4px" }}>
              {"ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").map(c => (
                <div key={c} style={{ minWidth: "22px", textAlign: "center", fontSize: "11px", color: "#5B7EA6", padding: "3px 0" }}>{c}</div>
              ))}
            </div>
            <div style={{ display: "flex", gap: "4px" }}>
              {"ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").map(c => (
                <div key={c} style={{ minWidth: "22px", textAlign: "center", fontSize: "11px", color: "#534AB7", fontWeight: 600, padding: "3px 0", background: "#1A1440", borderRadius: "4px" }}>
                  {caesarShift(c, tab === "encrypt" ? shift : -shift)}
                </div>
              ))}
            </div>
          </div>
          <p style={{ fontSize: "10px", color: "#3A5070", marginTop: "8px", marginBottom: 0 }}>Top row = original · Bottom row = shifted</p>
        </div>
      )}

      {/* Brute force output */}
      {tab === "brute" && (
        <div style={card}>
          <label style={{ fontSize: "11px", color: "#F0997B", letterSpacing: "2px", display: "block", marginBottom: "10px" }}>
            ALL 25 POSSIBLE DECRYPTIONS
          </label>
          {!input && <p style={{ color: "#3A5070", fontSize: "13px" }}>Enter ciphertext above to see all possibilities.</p>}
          {input && bruteRows.map(({ key, result }) => (
            <div key={key} style={{ display: "flex", gap: "12px", alignItems: "center", padding: "6px 0", borderBottom: "1px solid #1D2A4A" }}>
              <span style={{ minWidth: "50px", fontSize: "11px", color: "#D85A30" }}>Key {key}</span>
              <span style={{ fontSize: "13px", color: "#fff", wordBreak: "break-all" }}>{result}</span>
            </div>
          ))}
          {input && <p style={{ fontSize: "10px", color: "#3A5070", marginTop: "10px" }}>Only 25 possible keys — this is why Caesar Cipher is not secure for real use.</p>}
        </div>
      )}

      <p style={{ textAlign: "center", fontSize: "10px", color: "#1D2A4A", marginTop: "1rem" }}>DecodeLabs · Batch 2026 · #Cryptography</p>
    </div>
  );
}
