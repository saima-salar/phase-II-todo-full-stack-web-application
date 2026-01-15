// frontend/lib/auth.ts
import { createAuthClient } from "better-auth/react";

export const auth = createAuthClient();

// Export types for convenience
export type { Session } from "better-auth";