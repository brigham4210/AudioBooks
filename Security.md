# Security

## Authentication & Authorization
- Enforce multi-factor authentication (MFA) for all privileged accounts
- Strong password / passphrase policy (length, complexity, rotation only when compromised)
- Prefer passwordless (FIDO2/WebAuthn) where possible
- Role-Based Access Control (RBAC) with least privilege
- Periodic access reviews and automatic removal of stale accounts
- Integrate OAuth 2.0 / OpenID Connect for federated identity
- Secure session management (HTTPOnly, Secure, SameSite cookies; short-lived tokens; refresh token rotation)
- Detect and block brute-force and credential stuffing (rate limiting, IP reputation)

## Data Protection
- Encrypt data in transit (TLS 1.2+; prefer TLS 1.3) and at rest (AES-256 or equivalent)
- Centralized secret management (vault; never hardcode secrets)
- Key management: rotation, separation of duties, hardware-backed storage (HSM / KMS)
- Use signed tokens (JWT with proper exp, aud, iss; avoid long-lived JWTs)
- Avoid sensitive data exposure in logs or error messages
- Apply database row/field-level encryption for highly sensitive attributes
- Implement backup encryption and secure offsite storage
- Data retention and secure deletion policies

## Input Validation & Application Security
- Centralized input validation (allowlist over blocklist)
- Parameterized queries / ORM to prevent SQL injection
- Output encoding to mitigate XSS (context-aware)
- CSRF protection (tokens + SameSite cookies)
- Protect against SSRF, path traversal, insecure deserialization
- Enforce content security policy (CSP), X-Frame-Options, X-Content-Type-Options, Referrer-Policy
- Implement rate limiting / throttling on critical endpoints
- Safe file upload handling (MIME/type validation, antivirus scanning, isolated storage)

## Infrastructure & Deployment Security
- Keep OS, runtime, dependencies patched (automated dependency scanning)
- Use minimal base images (distroless / slim)
- Infrastructure as Code (IaC) with policy scanning (e.g., Open Policy Agent)
- Network segmentation, least privilege security groups, firewalls
- Zero trust principles for internal services
- Harden configurations (disable unused services, enforce secure ciphers)
- Use container isolation and regular image vulnerability scanning
- Secrets injected at runtime (never baked into images)
- Secure CI/CD (signed artifacts, supply chain scanning, provenance attestation)
- DDoS protection and WAF in front of public endpoints

## Logging, Monitoring & Incident Response
- Centralized, immutable, and timestamped logs (correlate by trace IDs)
- Collect auth events, data access, config changes, errors, permission escalations
- Real-time alerting (SIEM integration)
- Anomaly detection (behavioral analytics, unusual geolocation access)
- Protect log integrity and restrict access (no PII in logs)
- Incident response runbooks and tabletop exercises
- Post-incident review with root cause analysis and corrective actions
- Audit trails retained per compliance requirements

## Secure Development Lifecycle (SDL)
- Threat modeling for new features
- Static (SAST), dynamic (DAST), and dependency (SCA) scans in pipeline
- Manual security code reviews for critical modules
- Secure coding guidelines and developer training
- Security unit/integration tests for auth, access control, and validation logic

## Privacy & Compliance
- Data classification and handling rules
- Minimize collection (data minimization)
- User consent and transparent data usage notices
- Support data subject rights (export/delete)
- Periodic compliance audits (e.g., GDPR, SOC 2, HIPAA if applicable)

## Resilience & Recovery
- Encrypted, tested backups with defined RPO/RTO
- Chaos/security drills (simulate service degradation)
- Redundancy for critical components (multi-zone/region)
- Versioned infrastructure rollbacks (immutable deployments)

## Continuous Improvement
- Maintain a vulnerability disclosure / security.txt policy
- Track security KPIs (MTTR for vulns, patch latency)
- Regular penetration tests and third-party assessments
- Update dependencies proactively (avoid end-of-life runtimes)

## Checklist Highlights
- Least privilege everywhere
- Default deny on network and access policies
- No plaintext secrets
- Short-lived tokens
- Comprehensive telemetry (metrics + logs + traces)
- Automated scanning + manual validation for critical flows

```// filepath: /Users/brigham4210/Documents/GitHub/AudioBooks/Security.md
# Security

## Authentication & Authorization
- Enforce multi-factor authentication (MFA) for all privileged accounts
- Strong password / passphrase policy (length, complexity, rotation only when compromised)
- Prefer passwordless (FIDO2/WebAuthn) where possible
- Role-Based Access Control (RBAC) with least privilege
- Periodic access reviews and automatic removal of stale accounts
- Integrate OAuth 2.0 / OpenID Connect for federated identity
- Secure session management (HTTPOnly, Secure, SameSite cookies; short-lived tokens; refresh token rotation)
- Detect and block brute-force and credential stuffing (rate limiting, IP reputation)

## Data Protection
- Encrypt data in transit (TLS 1.2+; prefer TLS 1.3) and at rest (AES-256 or equivalent)
- Centralized secret management (vault; never hardcode secrets)
- Key management: rotation, separation of duties, hardware-backed storage (HSM / KMS)
- Use signed tokens (JWT with proper exp, aud, iss; avoid long-lived JWTs)
- Avoid sensitive data exposure in logs or error messages
- Apply database row/field-level encryption for highly sensitive attributes
- Implement backup encryption and secure offsite storage
- Data retention and secure deletion policies

## Input Validation & Application Security
- Centralized input validation (allowlist over blocklist)
- Parameterized queries / ORM to prevent SQL injection
- Output encoding to mitigate XSS (context-aware)
- CSRF protection (tokens + SameSite cookies)
- Protect against SSRF, path traversal, insecure deserialization
- Enforce content security policy (CSP), X-Frame-Options, X-Content-Type-Options, Referrer-Policy
- Implement rate limiting / throttling on critical endpoints
- Safe file upload handling (MIME/type validation, antivirus scanning, isolated storage)

## Infrastructure & Deployment Security
- Keep OS, runtime, dependencies patched (automated dependency scanning)
- Use minimal base images (distroless / slim)
- Infrastructure as Code (IaC) with policy scanning (e.g., Open Policy Agent)
- Network segmentation, least privilege security groups, firewalls
- Zero trust principles for internal services
- Harden configurations (disable unused services, enforce secure ciphers)
- Use container isolation and regular image vulnerability scanning
- Secrets injected at runtime (never baked into images)
- Secure CI/CD (signed artifacts, supply chain scanning, provenance attestation)
- DDoS protection and WAF in front of public endpoints

## Logging, Monitoring & Incident Response
- Centralized, immutable, and timestamped logs (correlate by trace IDs)
- Collect auth events, data access, config changes, errors, permission escalations
- Real-time alerting (SIEM integration)
- Anomaly detection (behavioral analytics, unusual geolocation access)
- Protect log integrity and restrict access (no PII in logs)
- Incident response runbooks and tabletop exercises
- Post-incident review with root cause analysis and corrective actions
- Audit trails retained per compliance requirements

## Secure Development Lifecycle (SDL)
- Threat modeling for new features
- Static (SAST), dynamic (DAST), and dependency (SCA) scans in pipeline
- Manual security code reviews for critical modules
- Secure coding guidelines and developer training
- Security unit/integration tests for auth, access control, and validation logic

## Privacy & Compliance
- Data classification and handling rules
- Minimize collection (data minimization)
- User consent and transparent data usage notices
- Support data subject rights (export/delete)
- Periodic compliance audits (e.g., GDPR, SOC 2, HIPAA if applicable)

## Resilience & Recovery
- Encrypted, tested backups with defined RPO/RTO
- Chaos/security drills (simulate service degradation)
- Redundancy for critical components (multi-zone/region)
- Versioned infrastructure rollbacks (immutable deployments)

## Continuous Improvement
- Maintain a vulnerability disclosure / security.txt policy
- Track security KPIs (MTTR for vulns, patch latency)
- Regular penetration tests and third-party assessments
- Update dependencies proactively (avoid end-of-life runtimes)

## Checklist Highlights
- Least privilege everywhere
- Default deny on network and access policies
- No plaintext secrets
- Short-lived tokens
- Comprehensive telemetry (metrics + logs + traces)
- Automated scanning + manual validation for critical flows
