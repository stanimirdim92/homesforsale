Here’s your formatted content in Markdown:


### Tech
- [x] Python - Django with DRF
- [ ] Nginx - 
  - [ ] Load balancers, 
  - [ ] ASGI connector, 
  - [ ] static file serve.
- [ ] OAuth2 maybe with Keycloak
- [x] PostgreSQL 16+
- [ ] Logbook for logs
- [ ] Elasticsearch
- [ ] GraphQL
- [ ] Sass
- [ ] Typescript
- [ ] React
- [ ] Leaflet for interactive maps or Maxar
- [ ] Django Channels - Real-time communication with Django, enabling WebSockets.
- [ ] Celery - Task queue for handling asynchronous jobs.
- [ ] PostGIS - Geographic object extensions for PostgreSQL.
- [ ] Zoopla
- [ ] Rightmove APIs: If you want to pull in real estate data from these sources (depending on their availability for your region).




### Infrastructure
- AWS - RDS
- AWS - S3
- AWS - EC2
- Imgix - ?

### DevOps
- [x] Git
- [x] IntelliJ
- [ ] Github / Actions
- [ ] Kubernetes - Container orchestration platform for automating application deployment.
- [ ] Docker
- [ ] Kafka and/or Apache Spark
- [ ] Hadoop - Framework for processing large datasets in distributed computing environments.
- [x] Redis still needs configuration
  - [ ] (Cluster for later?).
- [ ] Kibana?
- [ ] Onelogin?
- [ ] Terraform
- [ ] CircleCI - Continuous integration and delivery (CI/CD).
- [ ] Jenkins - Open-source automation server for CI/CD pipelines.
- [ ] ArgoCD - GitOps continuous delivery for Kubernetes.
- [ ] Ansible - Automation platform for configuration management.
- [ ] Puppet - IT automation software for managing configurations.
- [ ] Chef - Configuration management tool for automation.
- [ ] Consul - Service discovery, monitoring, and configuration.
- [ ] Vault - Securely store and access secrets, tokens, API keys, and certificates.
- [ ] Elastic Stack (ELK) - Elasticsearch, Logstash, and Kibana for log management.
- [ ] Fluentd - Unified logging layer for cloud environments.

### AI
- [ ] Langchain
- [ ] Langsmith
- [ ] Langgraph
- [ ] OpenAI
- [ ] Pandas

### Monitoring
- [ ] Sentry
- [ ] Prometheus
- [ ] Airflow
- [ ] Kibana
- [ ] Grafana
- [ ] Datadog - Full-stack monitoring and security.
- [ ] New Relic - Application performance monitoring (APM) for cloud environments.
- [ ] Elastic APM - Distributed tracing and performance monitoring for applications.
- [ ] Honeycomb - Observability for understanding complex systems.
- [ ] Zabbix - Open-source monitoring solution for networks and applications.
- [ ] Nagios - Infrastructure monitoring for servers and networks.
- [ ] Splunk - Log management and monitoring, with machine learning-driven insights.
- [ ] AppDynamics - Performance monitoring for apps and business metrics.


### Payment Systems
- [ ] Stripe
- [ ] Revolut
- [ ] Paypal
- [ ] Bank

### Architecture
- [ ] Archimate

### Business Tools
- [ ] Jira
- [ ] Confluence
- [ ] Zendesk - for customer live support and internal communication.

### Analytics
- [ ] Mixpanel - Product and behavioral analytics.
- [ ] Hotjar - Heatmaps and user session recordings for behavior analysis.
- [ ] Heap - Automatically captures every event in a product for detailed analytics.
- [ ] Amplitude - Product analytics to understand user behavior and engagement.
- [ ] Segment - Customer data platform for collecting and routing analytics data.
- [ ] Looker - Business intelligence and data exploration.
- [ ] BigQuery - Google’s fully-managed, serverless data warehouse for analytics.
- [ ] Tableau - Data visualization and business intelligence.
- [ ] FB Pixel
- [ ] Tiktok
- [ ] Google Analytics
- [ ] Google Tag Manager
- [ ] Google Ads
- [ ] Twitter
- [ ] Reddit


---

# Todo
- [ ] [Werkzeug Documentation](https://werkzeug.palletsprojects.com/en/2.3.x/)
- [ ] [Django ASGI Deployment with Uvicorn](https://docs.djangoproject.com/en/dev/howto/deployment/asgi/uvicorn/)
- [ ] [Django ASGI Deployment with Hypercorn](https://docs.djangoproject.com/en/dev/howto/deployment/asgi/hypercorn/)
- [ ] Finish configs
- [ ] Finish testing setup - pytest
- [ ] Finish Docker
- [ ] Finish Black and Flake8
- [ ] Add Anymail
- [ ] setup mypy
- [ ] black
- [ ] flake
- [ ] isort
- [ ] Content Delivery Network (CDN): Utilize CDNs like Cloudflare or Akamai to improve content load times globally.
- [ ] Third-Party Integrations: Incorporate services like Twilio for SMS notifications or SendGrid for email communications.


### Current used technologies
- Python 3.12+
- Django 5.1+
- djangorestframework 3.15+
- django-debug-toolbar 5.0+ - for debug test
- django-allauth - Login, 2FA etc.
- redis[hiredis] - caching is important
- psycopg3[pool, binary] - for PostgreSQL v16
- Click - for command line tools - no commands yet, but planned
- lxml - for XML parsing and security
- requests - for HTTP requests # change to httpx
- pytest - for testing - no test yet
- celery - for asynchronous tasks - not installed yet
- asyncio - for asynchronous tasks
- django-oauth-toolkit - for OAuth
- rosseta for languages
- django-storages for S3  - not installed yet
- 
### Features
- Login / Registration for user/ agent
- Notifications
- Notes
- Favorites
- PM
- Saved Searches
- Find an agent with search
- my listings
- blacklist?
- wallet?
- invoices?
- account close/delete?
- push notifications?
- **Interactive Map Search:** 
  - Provide an intuitive map-based property search where users can draw areas they’re interested in, similar to Zoopla or Zillow.
   
- **AI-Powered Property Recommendations:**
  - Use machine learning to recommend properties based on user preferences and browsing history.
  - Example: "If you liked this property, you may also like..."

- **Comprehensive Property Filters:**
  - Enable advanced search filters, like neighborhood safety score, school ratings, proximity to transport, etc.

- **Analytics Dashboard for Agencies:**
  - Offer agencies insights into property views, click-through rates, and engagement analytics, giving them a clear understanding of the performance of their listings.
   
- **Heatmaps & Market Trends:**
  - Display price trends, neighborhood popularity, and average property appreciation rates. A heatmap feature can show popular areas based on user activity on the platform.
   
- **Property Price Estimation:**
  - Integrate a price estimation tool using available market data, historical price information, and AI to help sellers set a competitive price.
   
- **Virtual Tours & AR Integration:**
  - Offer 3D virtual tours and augmented reality for users to visualize the properties, improving the user experience.

- User Engagement Metrics: 
  - Show agents how their listings are performing with views, clicks, and inquiries analytics.

- Neighborhood Statistics: Include information on local schools, crime rates, public transportation, and amenities.
Structured Data: Use JSON-LD to provide structured data about the properties to search engines, improving visibility.
### **Do you need a license to operate a real estate website?**
   Generally, the website operator doesn't need a real estate license, but real estate agents and agencies listing properties on the platform will likely need proper licensing, depending on the country. Licensing laws vary within Europe, so it’s essential to verify the specific requirements for each country you plan to operate in. For example, in countries like France, Germany, and Spain, real estate agents need a professional license to operate, but as a platform owner, you are likely exempt from those regulations unless you directly engage in real estate transactions.
