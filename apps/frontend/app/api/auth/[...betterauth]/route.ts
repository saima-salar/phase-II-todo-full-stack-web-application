// frontend/app/api/auth/[...betterauth]/route.ts
import { auth } from "../../../../lib/better-auth-server";

// Handle requests using Better Auth's request handler
export const GET = async (req: Request, ctx: any) => {
  return auth(req, ctx);
};

export const POST = async (req: Request, ctx: any) => {
  return auth(req, ctx);
};