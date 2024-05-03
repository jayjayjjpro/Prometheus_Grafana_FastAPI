## Prometheus Configuration

This section outlines the key configurations for the Prometheus service within our deployment.

### Global Section

- **Scrape Interval**: Defines how frequently Prometheus scrapes data from targets.
- **Scrape Timeout**: Sets the timeout for each scrape attempt.
- **Evaluation Interval**: Specifies how often the alert rules are evaluated.

These settings apply globally unless overridden in specific jobs.

### Alerting Section

Configurations for how alerts are managed and communicated:
- **Follow Redirects**: Whether or not Prometheus will follow HTTP redirects.
- **Use HTTP/2**: Enables the use of HTTP/2 for communication.
- **Timeouts**: Sets timeouts for communicating with the Alertmanager.

### Scrape Configs Section

Defines specific scrape jobs for monitoring different services:

- **Prometheus Job**: 
  - **Job Name**: `prometheus`
  - **Description**: Scrapes metrics from the Prometheus server itself for self-monitoring.

- **FastAPI Job**:
  - **Job Name**: `fastapi`
  - **Description**: Configured to scrape metrics from a FastAPI application, providing insights into the web application's performance.

Each job can have customized `scrape_interval`, `scrape_timeout`, and other parameters to fine-tune the monitoring setup.
