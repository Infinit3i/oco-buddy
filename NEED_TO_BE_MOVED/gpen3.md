# Vulnerability Assessment and Penetration Testing

## Key Terms

- **Vulnerability**: A flaw or weakness that can be exploited by a threat actor  
  _Examples_: Buffer overflow, misconfiguration, design flaws

- **Exploit**: Code or technique that takes advantage of a vulnerability  
  _Examples_: Public exploit code, upload web shell to server

- **Threat**: An agent or actor that can cause harm  
  _Examples_: Human attacker, worm, user clicking on links

- **Risk**: Potential for loss or damage  
  _Formula_: Risk = Likelihood * Impact

- **Penetration Test (Pen Test)**: Identify security vulnerabilities that could allow an attacker to penetrate the environment or steal information

- **Red Team**: Designed to test detection and response capabilities

- **Purple Team**: A cross-functional team consisting of Red and Blue Teamers

- **Vulnerability Assessment**: Identify, quantify, and rank vulnerabilities without exploitation

- **Security Audit**: Testing against a rigorous set of standards

---

## The Goal of Pen Testing

- **MODEL** the techniques used by real-world attackers
- **FIND** vulnerabilities before adversaries do
- **EXPLOIT** those flaws under controlled circumstances  
  _In a professional, safe manner according to a carefully designed scope and Rules of Engagement_
- Determine **ORGANIZATIONAL RISK AND POTENTIAL IMPACT**
- Help the organization **IMPROVE SECURITY PRACTICES**

---

## Types of Penetration Tests

- Network services test (one of the most common)
- Assumed breach test
- Web application test
- Social engineering test (email-based or phone-based)
- Wireless security test (not just Wi-Fi)
- Physical security test
- Product security test (could be software package or hardware, e.g., IoT)
- Breaking or bypassing encryption on local data or intercepted traffic

---

## Common Attack Phases

For both pen testers and malicious attackers:
1. Recon
2. Footprinting and Scanning
3. Exploitation
4. Post-exploitation

- Malicious attackers and Red Teams often go further:
  - Maintaining access
  - Covering tracks with covert channels and log editing
- These phases aren't always followed in order; the best attackers jump around pragmatically.

---

## Overall Penetration Testing Process

### Preparation
- Sign a non-disclosure agreement (NDA), if applicable.
- Discuss the nature of the test with target personnel:
  - Identify salient threats and business concerns
  - Agree on Rules of Engagement
  - Determine the scope of the test
- Sign off on permission and notify about testing risks.
- Assign the testing team.

### Testing
- Conduct the test.

### Conclusion
- Perform detailed analysis and retest.
- Reporting and possible presentation.

---

## Documented Permission

Documented permission is **CRITICAL** for pen testers:
- **Internal Testers**: Use an internal permission memo or "get out of jail free card" if it's not part of the job description.
- **External Testers**: More protections and assurances are needed:
  - Contract language limiting liability should include indemnification clauses, acceptance of potential risks, and ownership of intellectual property.
  - Include pricing, payment terms, and other business requirements.
  - Insurance: Liability, errors and omissions, cyber/breach.

**Operate ONLY within a CLEARLY DEFINED scope** against targets for which you have **EXPLICIT** permission from their owners/operators, and **FOLLOW THE LAW**!

---

## Pre-Engagement Steps

1. **Goals**: Discuss the goals of the test to frame further discussions.
   - Important data and/or processes
   - Why is the test being performed?
   
2. **Type of Tests**: What type of test do they need? (Network, Web, SE, etc.)
  
3. **Scope**:
   - In-scope IP addresses, subnets, URLs, people/roles (social engineering)
   - Select exclusions
  
4. **Rules of Engagement**:
   - Usually a checklist
   - Add additional exclusions or exceptions
  
5. **Kickoff Call**: Final planning and establish communication channels.

---

## Goals

- Always ask what **DATA OR PROCESS IS MOST IMPORTANT**.
- It is alright to **ASK QUESTIONS** and get expected answers rather than **ASSUME AND BE WRONG**.
- This focuses the rest of the discussion and assessment:
  - Higher value penetration test
  - Focus on organizational goals, not technical goals (e.g., Domain Admin)
  
- Also, ask why they are doing the test (e.g., compliance, audit, new systems).
- Goals will guide the rest of the discussion.  
_(If the penetration testers DON'T ASK your goals, FIND NEW TESTERS!)_  
_The goal is NOT Domain Admin; the goal is what's important to that organization!_

---

## Scope

- What is to be tested?
  - Network address ranges or hosts
  - Specific domain names
  - Particular applications

- **Exclusions**: What should be explicitly avoided?
- **Third Parties**: Get permission from third parties before testing (cloud providers, third-party managed routers, switches, firewalls, etc.).
- Check when additional items are discovered before attacking them.
- A tight definition here helps prevent "scope creep" or missed targets.
- Penetration tests are typically time-boxed to one to three weeks.  
_(You're the one under the threat of handcuffs, NOT the organization; always check if newly discovered items are attackable with the organization.)_

---

## Rules of Engagement

- **PRE-APPROVE SAFER ATTACKS**: Scanning, password guessing, etc.
- Attacks with an **ELEVATED CHANCE OF A NEGATIVE IMPACT** require **SPECIFIC APPROVAL** and/or testing during a maintenance window.
  - Ensure it is documented (email is usually fine).
  
- **Denial-of-service (DoS)** is rarely authorized:
  - Asking is likely a wasted effort unless you have a specific useful attack.
  
- Agree on dates and times for testing:
  - Testing dates should never be a surprise.
  - Off-hours testing may incur additional costs (35%).

---

## Announced vs. Unannounced Tests

- Will the target's system admins, security team, hunt team, and incident handlers be informed of the test?
- Or will their response to a surprise test be measured?
- There are benefits to both, but be careful with an unannounced test!
  - Defenders may discover the scans and then shun all traffic.
  - Actions taken after being shunned are useless (waste of time/money).
  - If shunned, what happens next?

---

## Zero-Knowledge vs. Full-Knowledge Testing

- Will the testers be given network diagrams and system information?
- **Reasons for zero-knowledge testing**:
  - "More like the real-world attackers" - but is that true?
  - Non-existent or deficient architecture documentation.
  
- **Reasons for full-knowledge or partial knowledge testing**:
  - More efficient and cost-effective.
  - Attackers may have this info (dumpster diving, insider attacks, time).
  - Less chance of an error causing damage to systems.
  
- Hybrid approaches are possible but take more time (costlier).  
  _Daily debriefing can help foster knowledge transfer._  
  _We're the attackers, they're the defenders, BUT WE ARE ON THE SAME TEAM!_

---

## Be Careful Viewing Data on Compromised Systems

- **PHI**: Are you a medical practitioner in care of the patient? (NO!)
- **PII**: Be very careful with credit card and banking information.
- **HIPAA, GLBA, GDPR**: Technically, you breach if you access this data.
  
- **Intellectual Property**: How should you handle this sensitive data?
  - Accidents happen, so be careful.
  - Do NOT include sensitive data in the report (redact!).
  - Demonstrate access and quantity (access to a DB table and record count).

---

## Kickoff Call

- Go over the test scope and Rules of Engagement (ROE) as a reminder to everyone.
- Exchange contact info (name, role, mobile/cell, availability).
  - The pen testing team may notice erratic behavior or crashes in a target system.
  - A penetration test might discover evidence of previous intrusions.
  - An intruder could be attacking at the same time; the target needs deconfliction.
  
- Agree upon a secure data transmission method for the report, vulnerability data, passwords, etc.:
  - Encrypted email, secure content management (e.g., Box), GPG/PGP (less common), encrypted ZIP (less secure due to shared passwords and leakage of filenames).
  
- Schedule debriefing calls.

---

## Building a Lab

- Use VMs: Easily revert, store, clone, and build systems.
- Servers: Windows Domain, File Shares, IIS; multiple Linux distros.
- End user: Windows 10, 11.
- **Licensing**:
  - **Linux**: Typically free. RHEL requires a paid subscription, but Fedora is very similar.
  - **Windows**: Use free trials or pay for a license.

---

## Systems Used for Internal Testing

- **Physical**: Laptop or minicomputer
  - Use full-disk encryption (FDE) or scrub unencrypted data before return shipping.
  - Note: Internal policies often allow corporate-owned devices on the network but require extra paperwork for third-party-owned devices.
  
- **Virtual**: Custom VM 
  - Target is responsible for destruction.
  - Requires internal team to provision, set up, and configure.

---

## Dedicated Test Systems