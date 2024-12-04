# Duruş Takibi

## Database MYSQL

```sql
CREATE DATABASE maintenance_db;
USE maintenance_db;

CREATE TABLE faults (
    id INT AUTO_INCREMENT PRIMARY KEY,
    robot_name VARCHAR(50) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    fault_reason VARCHAR(200) NOT NULL,
    changed_part VARCHAR(100),
    downtime FLOAT NOT NULL,
    lost_production INT NOT NULL
);

CREATE TABLE statistics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    robot_name VARCHAR(50) NOT NULL,
    total_downtime FLOAT NOT NULL,
    total_lost_production INT NOT NULL
);
```

---
Geliştirilebilir duruş takip sistemi.
