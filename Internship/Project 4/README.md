# 🛡️ System Vulnerability Checklist — Blue Team Audit Toolkit

> DecodeLabs Cyber Security Industrial Training | Batch 2026 | Project 4 (Optional Mastery)

\---

## 📌 Overview

Project 4 is the **Optional Mastery Phase** of the DecodeLabs Cyber Security Industrial Training. While the first three projects focused on building defensive tools, this project turns the auditor's eye inward — you run the 4-step vulnerability checklist on your own primary computer and deliver a professional **1-page Vulnerability Report** documenting exactly what you found and fixed.

> \\\*"This is not a theoretical exercise. You cannot defend an enterprise if you cannot secure your own perimeter."\\\* — DecodeLabs Project 4 Brief

\---

## 🎯 Project Goals

* Run a structured 4-step security audit on your own system
* Identify vulnerabilities using real CLI commands (PowerShell / Terminal)
* Score each finding using the CVSS 4.0 framework
* Document findings, remediation actions, and hardened verification
* Deliver a professional 1-page Vulnerability Report

\---

## 🧠 The Blue Team Mindset

|Legacy View|Blue Team Mindset|
|-|-|
|Security as a Product|Security as a Continuous Process|
|Defending single components|Proactive hunting|
|Reactive remediation|Assuming constant software decay|
|Assuming the perimeter is secure|Mitigating zero-day exploits|

> \\\*"A system's integrity is dynamic. The security auditor is the essential gatekeeper for organizational resilience."\\\*

\---

## 🗂️ Project Structure

```
project-4-vulnerability-checklist/
├── vulnerability\\\_checklist.py       # Automated Python audit tool (cross-platform)
├── vulnerability\\\_checklist.html     # Interactive browser-based checklist (AI-assisted)
└── README.md                        # This file
```

\---

## ⚙️ The 4-Step Checklist Framework

The audit follows an IPO model:

```
Input                    →   Process                  →   Output
Establishing Baseline        Methodical Inspection        Threat Reporting
(Determine system state)     (Cross-reference checklist)  (Risk-ranked vuln list)
```

> Axiom: \\\*You cannot secure an asset that you do not know exists.\\\* (CIS Controls 1 \\\& 2)

\---

## 📋 Step 1 — The Identity Front Door

**Focus:** Password policy and Multi-Factor Authentication (MFA) configuration.

### Passwords — Legacy vs NIST 800-63B

||Legacy Protocol|NIST 800-63B Standard ✅|
|-|-|-|
|**Policy**|Complex rules + forced periodic expiration|Strong passphrases, no forced expiration unless compromised|
|**Focus**|Character complexity|Human memory and length|

### MFA — Legacy vs NIST 800-63B

||Legacy Protocol|NIST 800-63B Standard ✅|
|-|-|-|
|**Method**|SMS / voice OTP codes|FIDO2 / WebAuthn / Passkeys|
|**Risk**|Vulnerable to interception and MFA fatigue|Tied to cryptographic device keys — phishing-resistant|

### Checklist Items

|Check|CVSS|Command|
|-|-|-|
|Guest Account disabled|7.5 HIGH|`dscl . -read /Users/Guest` (macOS) · `net user Guest` (Windows)|
|Admin group audited|6.5 MEDIUM|`dscl . -read /Groups/admin GroupMembership` (macOS) · `Get-LocalGroupMember -Group "Administrators"` (Windows)|

**Why Guest Accounts Matter:** An enabled Guest account allows untrusted users to conduct basic reconnaissance or attempt privilege escalation attacks without credentials.

**Why Privilege Creep Matters:** Lingering admin memberships from old roles create unnecessary attack surface. Every extra admin account is a potential pivot point for attackers.

\---

## 📋 Step 2 — Software Decay \& Patch Management

**Focus:** OS updates, browser patches, and Shadow IT.

> \\\*\\\*The Auditor's Rule:\\\*\\\* Delaying an update is explicitly accepting a risk.

### Audit Objectives

* Verify automated OS updates are enforced
* Identify unpatched browser builds and out-of-date antivirus databases
* Hunt for Shadow IT — unapproved applications bypassing corporate restrictions

### Checklist Items

|Check|CVSS|Command|
|-|-|-|
|OS update status|7.8 HIGH|`softwareupdate -l` (macOS) · `Get-WUList` (Windows) · `apt list --upgradable` (Linux)|
|Application inventory|4.3 MEDIUM|`ls /Applications` (macOS) · `Get-ItemProperty HKLM:\\\\...\\\\Uninstall\\\\\\\*` (Windows)|

\---

## 📋 Step 3 — Auditing the Human Perimeter

**Focus:** System misconfigurations and physical/behavioral hygiene.

### System Misconfigurations

**Guest Account Threat (Deprecated/High Risk)**
Disabling guest accounts prevents untrusted users from conducting basic reconnaissance or utilizing privilege escalation attacks.

**Privilege Creep**
Check for unchecked, lingering Admin group memberships. Enforce Least Privilege — no account should have more access than it actively needs.

### Physical \& Behavioral Hygiene

**Physical Security**

* Verify screen locking timeouts (5 minutes maximum)
* Check for local credential storage (sticky notes, unencrypted files)
* Check for rogue USB peripherals

**AI-Driven Social Engineering**
By 2026, deepfakes and cloned voices are corporate-scale threats. Auditors must verify employee reliance on secondary, trusted communication channels.

### Checklist Items

|Check|CVSS|Command|
|-|-|-|
|Screen lock timeout|5.5 MEDIUM|`defaults -currentHost read com.apple.screensaver idleTime` (macOS)|

\---

## 📋 Step 4 — Network \& Endpoint Hygiene

**Focus:** Firewall controls and disk encryption.

### The Shield — Inbound Traffic Controls

**Focus:** OS Firewall.

**Action:** Verify the firewall is active and blocking unauthorized inbound traffic.

On macOS, ensure the Application Firewall (ALF) is active **and** Stealth Mode is enabled to prevent the system from responding to external reconnaissance pings.

### The Vault — Data at Rest

**Focus:** Local Disk Encryption.

**Action:** Validate that the entire local disk is encrypted to protect data in the event of physical theft.

|Check|CVSS|Command|
|-|-|-|
|OS Firewall active|8.1 HIGH|`socketfilterfw --getglobalstate` (macOS) · `Get-NetFirewallProfile` (Windows)|
|Full disk encryption|7.3 HIGH|`fdesetup status` (macOS) · `Get-BitLockerVolume` (Windows)|

**Tools:** FileVault on macOS · BitLocker with TPM on Windows.

\---

## 🔧 The Auditor's Execution Matrix

|Security Check|Windows (PowerShell)|macOS (Terminal)|
|-|-|-|
|Verify Firewall|`Get-NetFirewallProfile`|`socketfilterfw --getglobalstate`|
|Check Encryption|`Get-BitLockerVolume`|`fdesetup status`|
|Audit Admin Rights|`Get-LocalGroupMember`|`dscl . -read /Groups/admin`|
|Find Shadow IT|`Get-ItemProperty HKLM:\\\\...\\\\Uninstall\\\\\\\*`|`ls /Applications`|
|Search for Updates|`Get-WUList`|`softwareupdate -l`|

\---

## 📊 CVSS Risk Classification

Risk is scored using the **CVSS 4.0 framework**, which evaluates Intrinsic Severity, Current Exploit Landscape, and Organizational Context.

|Risk Level|CVSS Score|Example Findings|Action|
|-|-|-|-|
|🔴 Critical|9.0 – 10.0|Unauthenticated RCE, databases without passwords|Fix immediately|
|🟠 High|7.0 – 8.9|Disabled firewall, no disk encryption, unpatched OS|Fix urgently|
|🟡 Medium|4.0 – 6.9|Excessive admin accounts, overly long screen lock|Schedule remediation|
|🟢 Low|0.1 – 3.9|Outdated non-essential apps (e.g., an intern's Spotify app)|Fix when possible|

\---

## 📄 The Vulnerability Report — Required Deliverable

The final deliverable is a professional 1-page Vulnerability Report with three mandatory sections:

### Section 1: Flaws Found (The Diagnosis)

Document at least **three specific security flaws** discovered using the CLI tools, including the CVSS score for each.

### Section 2: Remediation Actions (The Treatment)

Detail the exact steps taken to fix each flaw — e.g., enabling WPA3, deleting the Guest Account via terminal, updating a zero-day browser vulnerability.

### Section 3: Hardened Verification (The Proof)

Provide the final terminal outputs proving the system is now in a secure, hardened state. Example:

```
\\\[OK] FileVault is On.
\\\[OK] Firewall is enabled (State = 1).
\\\[OK] System Integrity Protection is enabled.
\\\[OK] Guest account: disabled.
```

\---

## ▶️ How to Run

### Python Automated Audit

```bash
python vulnerability\\\_checklist.py
```

Runs all 7 checks automatically, detects your OS, executes the appropriate CLI commands, and saves a formatted Vulnerability Report to a `.txt` file in the current directory.

### Interactive Browser Tool

Double-click `vulnerability\\\_checklist.html` — no install needed. Work through each step, mark your findings, and click **Generate Vulnerability Report** to produce the formatted report ready for submission.

\---

## 📋 Sample Report Output

```
======================================================================
  SYSTEM VULNERABILITY REPORT
  DecodeLabs Cyber Security — Project 4 | Batch 2026
======================================================================
  Date      : 2026-04-20 14:32
  Host      : MacBook-Pro.local
  OS        : Darwin 24.3.0
  Auditor   : DecodeLabs Intern — Batch 2026
  Checks    : 7 | Failures: 2 | Warnings: 1 | Passed: 4
======================================================================

  SECTION 1: FLAWS FOUND (The Diagnosis)
  ------------------------------------------------------------------
  \\\[1] OS Firewall Status  |  HIGH  |  CVSS: 8.1
      Step     : Step 4 — Network \\\& Endpoint
      Finding  : Firewall is DISABLED — system exposed to inbound reconnaissance.

  \\\[2] Full Disk Encryption Status  |  HIGH  |  CVSS: 7.3
      Step     : Step 4 — Network \\\& Endpoint
      Finding  : FileVault is OFF — data unprotected against physical theft.

  SECTION 2: REMEDIATION ACTIONS (The Treatment)
  ------------------------------------------------------------------
  \\\[1] OS Firewall Status
      Action   : sudo socketfilterfw --setglobalstate on
                 sudo socketfilterfw --setstealthmode on

  \\\[2] Full Disk Encryption Status
      Action   : System Settings → Privacy \\\& Security → FileVault → Turn On.

  SECTION 3: HARDENED VERIFICATION (The Proof)
  ------------------------------------------------------------------
  ✅  Guest Account Status: Disabled.
  ✅  Admin Privilege Audit: Only necessary accounts present.
  ✅  OS Software Update Status: System is fully up to date.
  ✅  Screen Lock Timeout: 300 seconds (5 min). Acceptable.
======================================================================
  Auditor Sign-off: All findings documented per CVSS 4.0 framework.
======================================================================
```

\---

## 📚 Key Concepts Learned

* Blue Team vs Red Team mindset — proactive vs reactive defense
* CVSS 4.0 risk scoring framework (Intrinsic, Threat, Environmental)
* NIST 800-63B password and MFA standards
* Privilege creep and the Least Privilege Principle
* Shadow IT detection and application inventory auditing
* OS firewall configuration: ALF on macOS, Windows Defender Firewall
* Full disk encryption: FileVault (macOS) and BitLocker with TPM (Windows)
* Physical security hygiene: screen lock, credential storage, USB risks
* AI-driven social engineering threats (deepfakes, cloned voices)
* Professional vulnerability report writing

\---

## 🛡️ Built With

* **Language:** Python 3 (standard library only — `subprocess`, `platform`, `datetime`)
* **Interactive Tool:** Vanilla HTML / CSS / JavaScript (AI-assisted)
* **Framework:** CVSS 4.0 · NIST 800-63B · CIS Controls
* **Program:** DecodeLabs Cyber Security Industrial Training — Batch 2026
* **Track:** Optional Mastery / Risk Assessment

\---

> — DecodeLabs Project 4 Brief

