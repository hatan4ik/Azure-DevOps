package remediation

default allow := false

safe_actions := {
  "restart_noncritical_deployment",
  "scale_nodepool_within_limit",
  "reconcile_configmap_from_git",
  "rollback_last_known_good",
  "renew_certificate_approved_path"
}

allow if {
  input.action in safe_actions
  input.environment == "nonprod"
}

allow if {
  input.action in safe_actions
  input.environment == "prod"
  input.service_criticality != "tier0"
  input.blast_radius == "low"
  input.has_rollback == true
  input.change_window_allowed == true
}
