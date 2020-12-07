val stage = taskKey[Unit]("Stage and clean task")

stage := {
  (stage in Universal).value
  if (sys.env.getOrElse("POST_STAGE_CLEAN", "false").equals("true")) {
    println("cleaning...")
    sbt.IO.delete(baseDirectory.value / "my-subdir")
  }
}