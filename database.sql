create table terminal_commands (
  id serial primary key,
  terminal_name text,
  command_name text,
  command text,
  command_detailed text,
  what_it_does text
)