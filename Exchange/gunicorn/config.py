# Server socket
bind = "0.0.0.0:8000"

# Workers
workers = 3
threads = 2
worker_class = 'sync'
timeout = 30

# Logging
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log errors to stderr
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Server options
forwarded_allow_ips = "*"
