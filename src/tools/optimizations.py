from api_connection import post
from models import (
    EstimateOptimizationRequest,
    CreateOptimizationRequest,
    ReadOptimizationRequest,
    ListOptimizationRequest,
    EstimateOptimizationResponse,
    UpdateOptimizationRequest,
    AbortOptimizationRequest,
    DeleteOptimizationRequest,
    ListOptimizationResponse,
    ReadOptimizationResponse,
    RestResponse
)

def register_optimization_tools(mcp):
    # Estimate cost
    @mcp.tool(
        annotations={
            'title': 'Estimate optimization time',
            'readOnlyHint': True,
        }
    )
    async def estimate_optimization_time(
            model: EstimateOptimizationRequest) -> EstimateOptimizationResponse:
        """Estimate the execution time of an optimization with the 
        specified parameters.
        """
        return await post('/optimizations/estimate', model)

    # Create
    @mcp.tool(
        annotations={
            'title': 'Create optimization',
            'destructiveHint': False
        }
    )
    async def create_optimization(
            model: CreateOptimizationRequest) -> ListOptimizationResponse:
        """Create an optimization with the specified parameters."""
        return await post('/optimizations/create', model)

    # Read a single optimization job.
    @mcp.tool(
        annotations={'title': 'Read optimization', 'readOnlyHint': True}
    )
    async def read_optimization(
            model: ReadOptimizationRequest) -> ReadOptimizationResponse:
        """Read an optimization."""
        return await post('/optimizations/read', model)

    # Read all optimizations for a project.
    @mcp.tool(
        annotations={'title': 'List optimizations', 'readOnlyHint': True}
    )
    async def list_optimizations(
            model: ListOptimizationRequest) -> ListOptimizationResponse:
        """List all the optimizations for a project."""
        return await post('/optimizations/list', model)

    # Update the optimization name.
    @mcp.tool(
        annotations={'title': 'Update optimization', 'idempotentHint': True}
    )
    async def update_optimization(
            model: UpdateOptimizationRequest) -> RestResponse:
        """Update the name of an optimization."""
        return await post('/optimizations/update', model)

    # Update the optimization status (stop).
    @mcp.tool(
        annotations={'title': 'Abort optimization', 'idempotentHint': True}
    )
    async def abort_optimization(
            model: AbortOptimizationRequest) -> RestResponse:
        """Abort an optimization."""
        return await post('/optimizations/abort', model)

    # Delete
    @mcp.tool(
        annotations={'title': 'Delete optimization', 'idempotentHint': True}
    )
    async def delete_optimization(model: DeleteOptimizationRequest) -> RestResponse:
        """Delete an optimization."""
        return await post('/optimizations/delete', model)
