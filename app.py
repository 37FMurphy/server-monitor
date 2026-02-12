from flask import Flask, render_template, jsonify
import psutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    # Get system stats
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # Get network stats
    net_io = psutil.net_io_counters()
    
    stats = {
        'cpu': cpu_percent,
        'memory_percent': memory.percent,
        'memory_used_gb': round(memory.used / (1024**3), 2),
        'memory_total_gb': round(memory.total / (1024**3), 2),
        'disk_percent': disk.percent,
        'disk_used_gb': round(disk.used / (1024**3), 2),
        'disk_total_gb': round(disk.total / (1024**3), 2),
        'network_sent_mb': round(net_io.bytes_sent / (1024**2), 2),
        'network_recv_mb': round(net_io.bytes_recv / (1024**2), 2),
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)


