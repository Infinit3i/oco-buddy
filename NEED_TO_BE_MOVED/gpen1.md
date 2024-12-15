# Background on Access in Penetration Testing

- In an **Assumed Breach**, testers start with access (laptop and account).
- Red Teamers must fight for initial access, often via client-side attacks and social engineering/phishing.
- In a traditional penetration test, testers start with only network connectivity (both internal and external).
- Testers are commonly asked to identify all vulnerabilities, even if not exploitable (overlaps with vulnerability assessment).

---

## Where Does Access Come From?

- Initial access most often occurs through one of four primary methods:
  1. Default credentials and guessable credentials (including breached credentials).
  2. Exploitable services.
  3. Social engineering and phishing with payloads.
  4. Supply chain attacks (not feasible for pen testers).
  
- Before guessing credentials or exploiting a service, testers need to know it exists, which was part of the focus of training.

---

## The Importance of Passwords

- Passwords remain the dominant form of authentication today:
  - Common on intranets.
  - Often used on internet-accessible systems such as VPNs, SSH, web applications, and email.
  
- Penetration testers and ethical hackers must understand password attacks at a fine-grained level, as they are a crucial component of the attack arsenal.

---

## Credential Stuffing

- Users often reuse passwords across their organization and third-party sites.
- Attackers extract usernames and passwords from a third-party breach and attempt to log in at the target organization.
- Good security practice dictates that each account should use a unique password, but many users find this difficult.
  - Solutions include "passwordless" login, two-factor authentication (2FA), and password vaults.

---

## Credential Databases

- Online services allow searching for compromised credentials:
  - Paid services like [dehashed.com](https://dehashed.com) and [leakcheck.net](https://leakcheck.net).
- Some penetration testers maintain their own databases.

---

## Types of Online Password Attacks

### Password Guessing (Traditional)

- Targets one account with many passwords.
- Increased likelihood of account lockouts.
- Often targets known admin accounts (e.g., root) as they often can't be locked out.

### Password Spray

- Targets one password across many accounts.
- An attacker only needs one account to gain a foothold.
- High likelihood that at least one user will have a guessable password.
- Can still lock out accounts if attempts are too rapid.

---

## Making Good Guesses with a Custom Dictionary

- Most password complexity requirements include uppercase, lowercase, and numbers (sometimes special characters).
- Use the current `<season><year>`:
  - Many organizations require password rotation every 90 days; users may use seasonal cues.
- Examples of common patterns:
  - Orgname1, Orgname2, Orgname3...
  - Password1, Password2, Password3...
  - Welcome1, Welcome2, Welcome3...
- Need a special character? Add a `!`.

---

## Guessing Usernames

- Focus on common usernames and statistically likely usernames.
  - Use names common to the region (e.g., US Census data).
  - Use formats discovered during the recon phase (e.g., jdoe, john.doe).
  
- Note that there is no lockout for invalid usernames, but it does generate extra logs.

---

## Account Lockout Considerations

- Account lockout policies must be considered before conducting any password guessing attack.
- Lockout is not an issue for password cracking, but monitoring by target personnel is advised.

### Account Lockout on Windows

- **Lockout Threshold**: Number of bad password attempts allowed.
- **Lockout Observation Window**: Minutes before the count resets.
- **Lockout Duration**: Minutes before the account is automatically re-enabled.
  
- To see these settings for a domain, run:  
