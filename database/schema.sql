
CREATE TABLE IF NOT EXISTS healing_history (
    id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    pillar_name VARCHAR(255) NOT NULL,
    session_id VARCHAR(100), -- UUID for test session grouping
    testcase_id VARCHAR(512) NOT NULL,
    original_locator TEXT NOT NULL,
    healed_locator TEXT NOT NULL,
    app_type VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_pillar ON healing_history(project_name, pillar_name);
CREATE INDEX IF NOT EXISTS idx_testcase_id ON healing_history(testcase_id);
CREATE INDEX IF NOT EXISTS idx_session_id ON healing_history(session_id);

CREATE TABLE IF NOT EXISTS saved_reports (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    configuration TEXT NOT NULL, -- Stored as JSON string
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users table for authentication and authorization
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(20) NOT NULL DEFAULT 'user',  -- 'admin' or 'user'
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);

CREATE TABLE IF NOT EXISTS settings (
    id SERIAL PRIMARY KEY,
    refresh_interval INTEGER DEFAULT 30,
    default_date_range VARCHAR(50) DEFAULT '7d',
    theme VARCHAR(50) DEFAULT 'auto',
    
    -- Branding
    company_name VARCHAR(255) DEFAULT 'AI Healing App',
    logo_url VARCHAR(512),
    
    -- Alert Thresholds
    spike_threshold_count INTEGER DEFAULT 10,
    spike_threshold_minutes INTEGER DEFAULT 5,
    flaky_threshold_count INTEGER DEFAULT 3,
    flaky_threshold_hours INTEGER DEFAULT 24,
    daily_quota_per_project INTEGER DEFAULT 100,
    
    email_enabled INTEGER DEFAULT 0,
    smtp_host VARCHAR(255),
    smtp_port INTEGER DEFAULT 587,
    smtp_username VARCHAR(255),
    smtp_password VARCHAR(255),
    smtp_from_email VARCHAR(255),
    alert_receiver_emails TEXT,  -- Comma-separated list of email addresses for alert notifications
    
    slack_webhook_url VARCHAR(512),
    notify_critical INTEGER DEFAULT 1,
    notify_daily INTEGER DEFAULT 0,
    notify_weekly INTEGER DEFAULT 1,
    
    retention_days INTEGER DEFAULT 90,
    auto_cleanup INTEGER DEFAULT 0,
    
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Test case metadata table for tracking flaky tests
CREATE TABLE IF NOT EXISTS test_case_metadata (
    id SERIAL PRIMARY KEY,
    testcase_id VARCHAR(512) NOT NULL UNIQUE,
    status VARCHAR(50) DEFAULT 'active',
    assignee VARCHAR(255),
    comments TEXT,
    flakiness_threshold INTEGER DEFAULT 3,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alerts table for tracking system alerts
CREATE TABLE IF NOT EXISTS alerts (\n    id SERIAL PRIMARY KEY,
    alert_type VARCHAR(50) NOT NULL,  -- 'spike', 'quota_exceeded', 'flaky_test', 'custom'
    severity VARCHAR(20) NOT NULL,     -- 'critical', 'warning', 'info'
    message TEXT NOT NULL,
    project_name VARCHAR(255),
    pillar_name VARCHAR(255),
    test_case_id VARCHAR(255),
    alert_metadata TEXT,  -- JSON string for additional context
    status VARCHAR(20) DEFAULT 'active', -- 'active', 'acknowledged', 'resolved', 'dismissed'
    acknowledged_at TIMESTAMP,
    acknowledged_by VARCHAR(255),
    resolved_at TIMESTAMP,
    resolved_by VARCHAR(255),
    dismissed_at TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


CREATE INDEX IF NOT EXISTS idx_alerts_status ON alerts(status);
CREATE INDEX IF NOT EXISTS idx_alerts_type ON alerts(alert_type);
CREATE INDEX IF NOT EXISTS idx_alerts_severity ON alerts(severity);
CREATE INDEX IF NOT EXISTS idx_alerts_created ON alerts(created_at);

-- Alert rules table for configurable alert conditions
CREATE TABLE IF NOT EXISTS alert_rules (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    rule_type VARCHAR(50) NOT NULL,  -- 'spike', 'quota', 'flaky', 'custom'
    condition TEXT NOT NULL,  -- JSON string with rule configuration
    channels TEXT NOT NULL,   -- JSON array: ['email', 'slack', 'dashboard']
    enabled INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
