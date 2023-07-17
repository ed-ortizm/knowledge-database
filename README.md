# Knowledge Database
## Overview

The database is designed to help organize my readings to keep up to date with trends in tech. Readings include papers, books, and blog posts from various disciplines. The goal is to store metadata about each reading material, including information such as title, type, publisher details, unique identifiers, short summaries, external summary references, timestamps, and tags. Additionally, insights derived from the materials are stored along with their associated reading stages, takeaways, and ideas.

## Schema Design

### Reading Material Table

The `reading_material` table serves as the central table to store metadata about each reading material. It includes attributes such as `material_id`, `title`, `material_type`, `publisher_id`, `publisher_link`, `unique_identifier`, `short_summary`, `external_summary_path`, `created_at`, and `updated_at`. The `material_id` is a unique identifier for each reading material, allowing easy referencing from other tables. The `publisher_id` column establishes a relationship with the `publishers` table, enabling efficient retrieval of publisher details. The `short_summary` attribute provides a fixed-length summary of the material, while the `external_summary_path` references the external storage location for more detailed summaries. The `created_at` and `updated_at` columns track the timestamps for when materials are added or modified.

### Publishers Table

The `publishers` table stores information about publishers. It contains attributes such as `publisher_id` and `name`. The `publisher_id` serves as a unique identifier for each publisher, while the `name` attribute represents the name of the publisher. This table establishes a relationship with the `reading_material` table to associate each reading material with its corresponding publisher.

### Insights Table

The `insights` table is designed to capture insights derived from the reading materials. It includes attributes such as `insight_id`, `material_id`, `reading_stage`, `takeaways`, and `ideas`. The `insight_id` is a unique identifier for each insight, and the `material_id` establishes a relationship with the `reading_material` table, linking the insight to its associated material. The `reading_stage` attribute captures the stage of reading for which the insight is generated, such as "skimming," "second pass," or "in-depth." The `takeaways` attribute stores an array of concrete insights derived from the material, while the `ideas` attribute stores potential applications or ideas related to the material.

### Material_Tags Table

The `material_tags` table represents a many-to-many relationship between reading materials and tags or categories. It consists of the `material_id` and `tag` attributes, allowing multiple tags to be associated with each reading material.

## Benefits of the Design

- **Efficient Organization**: The database design provides a structured approach to organize reading materials, allowing easy retrieval and management of metadata.
- **Flexible Summaries**: By storing both short summaries in the `reading_material` table and more detailed summaries in external storage, the design balances efficiency and flexibility.
- **Insight Tracking**: The `insights` table captures insights, reading stages, takeaways, and ideas, enabling the client to track and organize their learnings effectively.
- **Relationships and Integrity**: By establishing relationships between tables, such as the association between reading materials and publishers, data integrity is maintained, and efficient querying becomes possible.
- **Tagging and Categorization**: The inclusion of the `material_tags` table facilitates the assignment of multiple tags or categories to reading materials, allowing for better organization and retrieval.