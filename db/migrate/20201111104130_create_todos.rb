class CreateTodos < ActiveRecord::Migration[6.0]
  def change
    create_table :todos do |t|
      t.string :name
      t.text :text
      t.integer :importance
      t.references :topic, null: false, foreign_key: true

      t.timestamps
    end
  end
end
