-- Create the enumerated type reading_stage_enum
CREATE TYPE reading_stage_enum AS enum
    ('skimming', 'second_pass', 'in_depth');

-- Create the Publishers Table
CREATE TABLE publishers (
  publisher_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

-- Create the Reading Material Table
CREATE TABLE reading_material (
  material_id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  material_type TEXT NOT NULL,
  publisher_id INTEGER REFERENCES publishers(publisher_id),
  publisher_link TEXT,
  unique_identifier TEXT,
  short_summary TEXT,
  external_summary_path TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Insights Table
CREATE TABLE insights (
  insight_id SERIAL PRIMARY KEY,
  material_id INTEGER REFERENCES reading_material(material_id),
  reading_stage reading_stage_enum NOT NULL,
  takeaways TEXT[],
  ideas TEXT[]
);

-- Create the Material_Tags Table
CREATE TABLE material_tags (
  material_id INTEGER REFERENCES reading_material(material_id),
  tag TEXT NOT NULL
);
