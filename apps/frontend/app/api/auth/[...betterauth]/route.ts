// frontend/app/api/auth/[...betterauth]/route.ts
import { auth } from "../../../../lib/better-auth-server";

// Handle requests using Better Auth's request handler
export const GET = auth.handler;
export const POST = auth.handler;